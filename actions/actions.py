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
# import fr_core_news_md
from spacy.attrs import IS_ALPHA, IS_STOP, IS_PUNCT
nlp = spacy.load("fr_core_news_md")

ENIGMA_PKL = os.path.join("enigma.pkl")

BOT_USER_INFO = os.path.join("action_data", "bot_user_information.csv")

RIDDLE_RESULTS = os.path.join("action_data", "riddle_results.csv")

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
    token_solution_len = enigma_cat['Solution_length'].iloc[e]

    return (riddle_name, riddle, solution, token_solution_len)

def preprocess_spacy(sent: str) -> np.ndarray:
    """
    string preprocessing function which returns a numpy array of tokens
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

def answer_result(mark: int):
    """
    Get a int 0 <= mark <= 4
    return:
    0: the answer is wrong
    1: the answer is probably wrong
    2: not clear
    3: the answer is probably right
    4: the answer is right
    """

    messages = list()

    if mark == 0:
        messages.append("Dommage, c'est une mauvaise réponse !")
        messages.append("Et non, mauvaise réponse")

    elif mark == 1:
        messages.append("J'ai bien peur que cela soit une mauvaise réponse.")
        messages.append("Il me semble que cela soit une mauvaise réponse.")

    elif mark == 2:
        messages.append("Je ne suis pas tout à fait sûr de ta réponse.")
        messages.append("La réponse est difficile à évaluer.")

    elif mark == 3:
        messages.append("Sans en être entièrement sûr, je crois que ta réponse est correcte.")
        messages.append("Pas sûr et certains, mais je crois que ta réponse est correcte.")

    elif mark == 4:
        messages.append("C'est une excellente réponse !")
        messages.append("Bravo, c'est une bonne réponse !")

    message = np.random.choice(np.array(messages))
    return message

def compare_answer(solution: str, user_solution: str) -> tuple:
    """
    based on the cosine_test and spacy_vec_sim_test inicators, will returns
    wether the user answer to the riddle seems to be right or wrong.
    Return:
    - cosine_indicator: indicator based on cosine similarity
    - spacy_vec_sim_indicator: indicator based on spacy vector similarity
    - mark: mark attributed to the user solution
    - answer_result(mark): answer do display
    """
    # Cosine similarity indicator
    try:
        cosine_indicator = cosine_test(solution, user_solution)
    except:
        cosine_indicator = 0

    # Spacy vector similarity indicator
    spacy_vec_sim_indicator = spacy_vec_sim_test(solution, user_solution)

    mark = int

    if len(solution) == 1: # Only one token in the solution
        if cosine_indicator >= 1 and spacy_vec_sim_indicator >= 1:
            mark = 4

        if cosine_indicator > .6 or (cosine_indicator > 0 and spacy_vec_sim_indicator > .7):
            mark = 3

        if cosine_indicator > .3 or (cosine_indicator > 0 and spacy_vec_sim_indicator > .5):
            mark = 2

        elif cosine_indicator == 0 and spacy_vec_sim_indicator == 0:
            mark = 0

        else:
            mark = 1

    elif len(solution) == 2: # Excatly two tokens in the solution
        if cosine_indicator >= 1 and spacy_vec_sim_indicator >= 1:
            mark = 4

        elif cosine_indicator > .1 or spacy_vec_sim_indicator > .45:
            mark = 3

        elif cosine_indicator > .05 or spacy_vec_sim_indicator > .3:
            mark = 2

        elif cosine_indicator == 0 and spacy_vec_sim_indicator == 0:
            mark = 0

        else:
            mark = 1

    else: # More than two tokens in the solution
        if cosine_indicator >= 1 and spacy_vec_sim_indicator >= 1:
            mark = 4

        elif cosine_indicator > .5 or spacy_vec_sim_indicator > .5:
            mark = 3

        elif cosine_indicator > .2 or spacy_vec_sim_indicator > .2:
            mark = 2

        elif cosine_indicator == 0 and spacy_vec_sim_indicator == 0:
            mark = 0

        else:
            mark = 1

    return cosine_indicator, spacy_vec_sim_indicator, mark, answer_result(mark)

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

def save_riddle_results(riddle: str, solution: str, user_solution: str, token_solution_len: int, cosine_indicator: int, spacy_vec_sim_indicator: int, mark: int):

    row = [riddle, solution, user_solution, token_solution_len, cosine_indicator, spacy_vec_sim_indicator, mark]

    with open(RIDDLE_RESULTS, "a") as f:
        writer = csv.writer(f)
        writer.writerow(row)

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
            dispatcher.utter_message(template="utter_societe_mysterieuse")
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
                dispatcher.utter_message(template="utter_societe_mysterieuse")
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

        with open("enigma.pkl", 'rb') as f:
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

                    riddle_name, riddle, solution, token_solution_len = get_riddle(enigma_df, category[0])

                    token_solution_len = str(token_solution_len)

                    how_to_answer = "\n(Commencez par \"rep:\" puis écrivez votre réponse.)"

                    dispatcher.utter_message( "** " + riddle_name + " **" + "\n" + riddle + how_to_answer)

                    return [SlotSet("requested_slot", slot), SlotSet("riddle_solution", solution), SlotSet("riddle", riddle), SlotSet("token_solution_len", token_solution_len)]

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
        riddle = tracker.get_slot('riddle')
        token_solution_len = tracker.get_slot('token_solution_len')

        cosine_indicator, spacy_vec_sim_indicator, mark, message = compare_answer(riddle_solution, user_riddle_solution)

        save_riddle_results(riddle, riddle_solution, user_riddle_solution, token_solution_len, cosine_indicator, spacy_vec_sim_indicator, mark)

        dispatcher.utter_message(message)
        dispatcher.utter_message(f"La bonne réponse est :\n{riddle_solution}")

        return [SlotSet("riddle_category", None), SlotSet("riddle_solution", None), SlotSet("user_riddle_solution", None), SlotSet("riddle", None), SlotSet("token_solution_len", None)]

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
