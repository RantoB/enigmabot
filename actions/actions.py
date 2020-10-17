from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, ActionExecuted, UserUttered, FollowupAction
from rasa_sdk.forms import FormAction
import logging
logger = logging.getLogger(__name__)

import numpy as np
import pickle
import pandas as pd
import re
import csv
import os

import smtplib
from email.mime.text import MIMEText

import spacy
import fr_core_news_md
from spacy.attrs import IS_ALPHA, IS_STOP, IS_PUNCT
nlp = spacy.load("fr_core_news_md")


ENIGMA_PKL = os.path.join("actions", "enigma.pkl")

BOT_USER_INFO = os.path.join("bot_user_info", "bot_user_information.csv")

SERVER = 'ssl0.ovh.net'
PORT = 465
SENDER = os.environ.get('LOGIN_ENIGMASTRAS_MAILBOX')
PSW = os.environ.get('PASSWORD_ENIGMASTRAS_MAILBOX')

def get_riddle(enigma_df: pd.core.frame.DataFrame, category: str):
    """
    for a given category, will return a random riddle, its name and its solution
    from the enigma_df dataframe
    """
    enigma_cat = enigma_df[enigma_df['Category'] == category]
    e = np.random.randint(0, enigma_cat.shape[0])
    riddle_name = enigma_cat['Title'].iloc[e]
    riddle = enigma_cat['Riddle'].iloc[e]
    solution = enigma_cat['Solution'].iloc[e]
    return (riddle_name, riddle, solution)

def preprocess_spacy(sent: str) -> np.ndarray:
    """string preprocessing function which returns a numpy array of tokens
    """
    doc = nlp(sent)
    tokens = np.char.lower(np.array([token.text for token in doc]))
    return tokens[~doc.to_array([IS_STOP]).astype(bool) * \
~doc.to_array([IS_PUNCT]).astype(bool)]

def cosine_test(sentence_1: str, sentence_2: str) -> float:
    """
    return a value which is a similarity indicator to check riddle solutions
    based on cosine similarity
    """

    sentence_1 = " ".join(preprocess_spacy(sentence_1))
    sentence_2 = " ".join(preprocess_spacy(sentence_2))

    vectorizer = TfidfVectorizer()
    tf_idf = vectorizer.fit_transform([sentence_1, sentence_2]).toarray()
    pd.DataFrame(data = tf_idf, columns=vectorizer.get_feature_names())

    return cosine_similarity(tf_idf)[1, 0]

def spacy_vec_sim_test(sentence_1: str, sentence_2: str) -> float:
    """
    return a value which is a similarity indicator to check riddle solutions
    based on spacy vector similarity
    """
    sentence_1 = " ".join(preprocess_spacy(sentence_1))
    sentence_2 = " ".join(preprocess_spacy(sentence_2))

    sentence_1 = nlp(sentence_1)
    sentence_2 = nlp(sentence_2)

    sim = list()
    for token_1 in sentence_1:
        for token_2 in sentence_2:
            sim.append(token_1.similarity(token_2))
    sim = np.array(sim)

    if len(sim) == 0:
        return 0
    elif len(sim) == 1:
        return sim[0]
    else:
        return (np.sort(sim)[-1] + np.sort(sim)[-2]) / 2

def check_answer(solution: str, user_solution: str) -> bool:
    """
    based on the cosine_test and spacy_vec_sim_test inicators, will returns
    wether the user answer to the riddle seems to be right or wrong.
    """
    try:
        indicator_1 = cosine_test(solution, user_solution)
    except:
        indicator_1 = 0

    indicator_2 = spacy_vec_sim_test(solution, user_solution)

    solution = preprocess_spacy(solution)

    if len(solution) == 1:
        if indicator_1 > .6 or (indicator_1 > 0 and indicator_2 > .7):
            return True
        else:
            return False

    elif len(solution) == 2:
        if indicator_1 > .1 or indicator_2 > .45:
            return True
        else:
            return False

    else:
        if indicator_1 > .5 or indicator_2 > .5:
            return True
        else:
            return False

def send_mail(receiver: str, subject: str, body: str):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg['To'] = receiver

    with smtplib.SMTP_SSL(SERVER, PORT) as smtp:
        smtp.login(SENDER, PSW)
        smtp.sendmail(SENDER, receiver, msg.as_string())
    return None

def save_information(user_name: str, user_email: str):
    with open(BOT_USER_INFO, "a") as f:
        writer = csv.writer(f)
        writer.writerow([user_name, user_email])
    return None

class ActionWhichGame(Action):

    def name(self) -> Text:
        return "action_which_game"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        which_game = "Il existe deux parcours, par quel jeu êtes-vous intéressé ?"
        game_1 = "La Société Mystérieuse de Strasbourg"
        game_2 = "1913, Meurte à la Krutenau"

        buttons = [{"title": game_1, "payload": game_1},
            {"title": game_2, "payload": game_2}]

        dispatcher.utter_button_message(which_game, buttons)

        return []

class ActionRequestedGame(Action):

    def name(self) -> Text:
        return "action_requested_game"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        game = tracker.get_slot("game")

        if game.lower() == "société mystérieuse de Strasbourg".lower():
            dispatcher.utter_message(template="utter_societe_musterieuse")
            dispatcher.utter_message(template="utter_next_game")
        else :
            dispatcher.utter_message(template="utter_meurtre_krutenau")
            dispatcher.utter_message(template="utter_next_game")

        return []

class ActionNextGame(Action):

    def name(self) -> Text:
        return "action_next_game"

    # @staticmethod
    # def start_story_events(deny):
    #     # type: (Text) -> List[Dict]
    #     return [ActionExecuted("action_listen")] + [UserUttered("/" + deny, {
    #         "intent": {"name": deny, "confidence": 1.0},
    #         "entities": {}
    #     })]
    # Trigger intent from a custom action:
    # https://forum.rasa.com/t/trigger-a-story-or-intent-from-a-custom-action/13784

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        deny_or_affirm = tracker.latest_message['intent'].get('name')

        if deny_or_affirm == 'affirm':

            game = tracker.get_slot("game")

            if game.lower() == "société mystérieuse de Strasbourg".lower():
                dispatcher.utter_message(template="utter_meurtre_krutenau")
                dispatcher.utter_message(template="utter_question_on_ENIGMA_Stras")
            else :
                dispatcher.utter_message(template="utter_societe_musterieuse")
                dispatcher.utter_message(template="utter_question_on_ENIGMA_Stras")

        elif deny_or_affirm == 'deny':
            dispatcher.utter_message(template="utter_question_on_ENIGMA_Stras")

        return []

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        active_form = tracker.active_form.get("name")

        if active_form == "form_riddle":
            logger.debug("The form '{}' is active".format(active_form))
            message = "Je n'ai pas pu interprêter votre réponse, pourriez-vous écrire \"Rep:\" puis écrire votre réponse ?"

            dispatcher.utter_message(message)

            return []

        elif active_form == "form_subscribe":
            requested_slot = tracker.get_slot("requested_slot")

            if requested_slot == "user_name":
                logger.debug("The form '{}' is active".format(active_form))
                message = "Je ne connais pas ce prénom, pourriez-vous écrire \"prénom:\" puis taper votre prénom, afni que je puisse le reconnaître?"

                dispatcher.utter_message(message)

            elif requested_slot == "user_email":
                logger.debug("The form '{}' is active".format(active_form))
                message = "Je ne reconnais pas le format de l'adresse mail, pourriez-vous écrire \"e-mail:\" puis taper votre adresse e-mail, afni que je puisse la reconnaître?"

                dispatcher.utter_message(message)

            return[]

        else:
            logger.debug("There is no active form")

            messages = []

            messages.append("Je ne suis pas sûr de comprendre, pourriez-vous reformuler ?")
            messages.append("Je suis désolé, je n'ai pas compris. Est-il possible de reformuler la quesion ?")
            messages.append("Excusez-moi mais je n'ai pas compris ce que vous demandez, est-ce que vous pourriez reformuler ?")
            messages.append("Attends voir... \nNon y'a quelque chose que je n'ai pas compris. Après tout je suis encore en apprentissage. Mais si vous reformulez, ça pourrait m'aider.")
            messages.append("J'ai bien peur de ne pas avoir compris... Est-ce bien en rapport avec ENIGMA Strasbourg ?")
            messages.append("Mhm, j'essaie pourtant de comprendre mais je ne suis pas sûr de bien sairir ce que vous cherchez à me demander. Peut-être qu'en reformulant j'arriverais à comprendre.")

            message = np.random.choice(np.array(messages))

            dispatcher.utter_message(message)

            return []

class ActionCheckActiveForm(Action):

    def name(self) -> Text:
        return "action_check_active_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        active_form = tracker.active_form.get("name")

        if active_form is not None:
            if active_form == "form_riddle":
                logger.debug("The form '{}' is active".format(active_form))
                message = "Je n'ai pas bien compris la réponse, pourriez-vous écrire \"Rep:\" puis écrire votre réponse ?"
                dispatcher.utter_message(message)
                return [FollowupAction("action_listen")]

            elif active_form == "form_subscribe":
                requested_slot = tracker.get_slot("requested_slot")

                if requested_slot == user_name:
                    logger.debug("The form '{}' is active".format(active_form))
                    message = "Je ne connais pas ce prénom, pourriez-vous écrire \"prénom:\" puis taper votre prénom, afni que je puisse le reconnaître?"

                    dispatcher.utter_message(message)
                    return [FollowupAction("action_listen")]

                elif requested_slot == user_email:
                    logger.debug("The form '{}' is active".format(active_form))
                    message = "Je ne reconnais pas le format de l'adresse mail, pourriez-vous écrire \"e-mail:\" puis taper votre adresse e-mail, afni que je puisse la reconnaître?"

                    dispatcher.utter_message(message)
                    return [FollowupAction("action_listen")]

            return []

class FormRiddle(FormAction):
    """Custom form action to fill the user riddle answer."""

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "form_riddle"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["riddle_category", "user_riddle_solution"]

    def request_next_slot(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Request the next slot and utter template if needed,
            else return None
            https://legacy-docs.rasa.com/docs/core/_modules/rasa_core_sdk/forms/"""

        with open(ENIGMA_PKL, 'rb') as f:
            enigma_df = pickle.load(f)

        categories = enigma_df['Category'].unique()
        buttons = list()
        for cat in categories:
            buttons.append({'title':cat, 'payload': cat})
        """
        -------------------------------------
        """
        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):
                logger.debug("Request next slot '{}'".format(slot))
                if slot == "riddle_category":
                    messages = list()
                    messages.append("Quelle genre d'énigme aimez-vous ?\n")
                    messages.append("Quelle genre d'énigme ?\n")
                    messages.append("Quelle type d'énigme ?\n")
                    message = np.random.choice(np.array(messages))

                    dispatcher.utter_button_message(message, buttons)
                    return [SlotSet("requested_slot", slot)]

                if slot == "user_riddle_solution":
                    category = tracker.get_slot('riddle_category')

                    riddle_name, riddle, solution = get_riddle(enigma_df, category[0])

                    how_to_answer = "\n(Commencez par \"rep:\" puis écrivez votre réponse.)"

                    dispatcher.utter_message( "** " + riddle_name + " **" + "\n" + riddle + how_to_answer)

                    return [SlotSet("requested_slot", slot), SlotSet("riddle_solution", solution)]

        """
        -------------------------------------
        """

        return None

    # def slot_mappings(self) -> Dict[Text, Any]:
    #     return {"riddle_category": self.from_entity(entity="riddle_category",
    #             intent=["inform_kind_of_riddle"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print the message"""

        user_answer = tracker.latest_message.get('text')
        user_riddle_solution = re.sub(r'Rep:.', '', user_answer)
        riddle_solution = tracker.get_slot('riddle_solution')

        if check_answer(riddle_solution, user_riddle_solution):
            message = f"Sans en être entièrement sûr, je crois que votre réponse est correcte.\
            \nLa bonne réponse est :\n{riddle_solution}"
        else:
            message = f"J'ai bien peur que cela soit une mauvaise réponse.\
            \nLa bonne réponse est :\n{riddle_solution}"

        dispatcher.utter_message(message)

        return [SlotSet("riddle_category", None), SlotSet("riddle_solution", None), SlotSet("user_riddle_solution", None)]

class FormSubscribe(FormAction):
    """Custom form action to fill the user riddle answer."""

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "form_subscribe"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["user_name", "user_email"]

    # def slot_mappings(self) -> Dict[Text, Any]:
    #     return {"riddle_category": self.from_entity(entity="riddle_category",
    #             intent=["inform_kind_of_riddle"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print the message"""

        user_name = tracker.get_slot('user_name')
        if type(user_name) == list:
            user_name = user_name[0]

        user_email = tracker.get_slot('user_email')
        if type(user_email) == list:
            user_email = user_email[0]

        # if tracker.get_slot('user_name') == None:
        #     user_answer = tracker.latest_message.get('text')
        #     user_name = re.sub(r'prénom:.', '', user_answer)
        # else:
        #     user_name = tracker.get_slot('user_name')[0]

        message = "name: {}\nemail: {}\nPouvez-vous confirmez que ces informations sont correctes ?".format(user_name, user_email)

        dispatcher.utter_message(message)

        return []

class ActionResetSubscribeSlots(Action):

    def name(self):
        return "action_reset_subscribe_slots"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("user_name", None), SlotSet("user_email", None)]

class ActionSaveInformation(Action):

    def name(self) -> Text:
        return "action_save_information"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_name = tracker.get_slot('user_name')
        if type(user_name) == list:
            user_name = user_name[0]

        user_email = tracker.get_slot('user_email')
        if type(user_email) == list:
            user_email = user_email[0]

        subject = "ENIGMA Strasbourg"
        body = f"\nBienvenue {user_name} !\nVotre addresse e-mail a bien été enregistrée et vous recevrez prochainement les actualités d'ENIGMA Strasbourg.\n\nMystérieusement..."

        send_mail(user_email, subject, body)

        save_information(user_name, user_email)

        message = "Votre adresse e-mail est bien enregistrée, vous allez recevoir un mail de confirmation."

        dispatcher.utter_message(message)

        return []
