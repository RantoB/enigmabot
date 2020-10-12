        # This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction
import logging
logger = logging.getLogger(__name__)

import numpy as np
import pickle
import pandas as pd
import re

# class ActionIntroduction(Action):
#
#     def name(self) -> Text:
#         return "action_introduction"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         name = tracker.get_slot("person")
#
#         if name == None:
#             latest_message = tracker.latest_message['text']
#             dispatcher.utter_message(f"Désolé, je ne connais pas ce prénom.\n Tu t'appelles {latest_message} ?")
#
#             return [SlotSet("person", latest_message)]
#
#         else:
#             dispatcher.utter_message(template="utter_introduce_greet_answer")
#             return []
#
# class ActionIntroductionInputToConfirm(Action):
#
#     def name(self) -> Text:
#         return "action_introduction_input_to_confirm"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         deny_or_affirm = tracker.latest_message['intent'].get('name')
#
#         if deny_or_affirm == "affirm":
#             dispatcher.utter_message("Ok")
#             dispatcher.utter_message(template="utter_introduce_greet_answer")
#             return []
#         elif deny_or_affirm == "deny":
#             dispatcher.utter_message("Comment est-ce que je peux t'appeler ?")
#             return [SlotSet("person", None)]
#
# class ActionForceIntroduction(Action):
#
#     def name(self) -> Text:
#         return "action_force_introduction"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         latest_message = tracker.latest_message['text']
#         SlotSet("person", latest_message)
#         dispatcher.utter_message(template="utter_introduce_greet_answer")
#
#         return [SlotSet("person", latest_message)]

def get_riddle(enigma_df: pd.core.frame.DataFrame, category: str):
    enigma_cat = enigma_df[enigma_df['Category'] == category]
    e = np.random.randint(0, enigma_cat.shape[0])
    riddle_name = enigma_cat['Title'].iloc[e]
    riddle = enigma_cat['Riddle'].iloc[e]
    solution = enigma_cat['Solution'].iloc[e]
    return (riddle_name, riddle, solution)

import spacy
from spacy.attrs import IS_ALPHA, IS_STOP, IS_PUNCT
nlp = spacy.load("fr_core_news_md")

def preprocess_spacy(sent: str) -> np.ndarray:
    doc = nlp(sent)
    tokens = np.char.lower(np.array([token.text for token in doc]))
    return tokens[~doc.to_array([IS_STOP]).astype(bool) * \
~doc.to_array([IS_PUNCT]).astype(bool)]

def cosine_test(sentence_1: str, sentence_2: str) -> float:
    sentence_1 = " ".join(preprocess_spacy(sentence_1))
    sentence_2 = " ".join(preprocess_spacy(sentence_2))

    vectorizer = TfidfVectorizer()
    tf_idf = vectorizer.fit_transform([sentence_1, sentence_2]).toarray()
    pd.DataFrame(data = tf_idf, columns=vectorizer.get_feature_names())

    return cosine_similarity(tf_idf)[1, 0]

def spacy_vec_sim_test(sentence_1: str, sentence_2: str) -> float:
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

class ActionWhichGame(Action):

    def name(self) -> Text:
        return "action_which_game"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        which_game = "Il existe deux parcours, par quel jeu es-tu intéressé ?"
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

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        deny_or_affirm = tracker.latest_message['intent'].get('name')

        if deny_or_affirm == 'affirm':

            game = tracker.get_slot("game")

            if game.lower() == "société mystérieuse de Strasbourg".lower():
                dispatcher.utter_message(template="utter_meurtre_krutenau")
                dispatcher.utter_message(template="utter_sth_else")
            else :
                dispatcher.utter_message(template="utter_societe_musterieuse")
                dispatcher.utter_message(template="utter_sth_else")

        elif deny_or_affirm == 'deny':
            dispatcher.utter_message("Ok,")
            dispatcher.utter_message(template="utter_sth_else")

        return []

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.active_form.get("name") is not None:
            logger.debug("The form '{}' is active".format(tracker.active_form))
            message = "Je n'ai pas bien compris la réponse, pourrais-tu écrire \"Rep:\" puis écrire ta réponse ?"

            dispatcher.utter_message(message)

            return [] #[FollowupAction("form_riddle")]

        else:
            logger.debug("There is no active form")

            messages = []

            messages.append("Je ne suis pas sûr de comprendre, pourrais-tu reformuler ?")
            messages.append("Je suis désolé, je n'ai pas compris. Est-il possible de reformuler la quesion ?")
            messages.append("Excuse-moi mais je n'ai pas compris ce que tu demandes, est-ce que tu pourrais reformuler ?")
            messages.append("Attends voir... \nNon y'a quelque chose que je n'ai pas compris. Après tout je suis encore en apprentissage. Mais si tu reformules ça pourrait m'aider.")
            messages.append("J'ai bien peur de ne pas avoir compris... Est-ce bien en rapport avec ENIGMA Strasbourg ?")
            messages.append("Mhm, j'essaie pourtant de comprendre mais je ne suis pas sûr de bien sairir ce que tu cherches à me demander. Peut-être qu'en reformulant j'arriverai à comprendre.")

            message = np.random.choice(np.array(messages))

            dispatcher.utter_message(message)

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

        with open('enigma.pkl', 'rb') as f:
            enigma_df = pickle.load(f)

        categories = enigma_df['Category'].unique()
        buttons = list()
        for cat in categories:
            buttons.append({'title':cat, 'payload': cat})
        """
        -------------------------------------
        """
        for i, slot in enumerate(self.required_slots(tracker)):
            if self._should_request_slot(tracker, slot):
                logger.debug("Request next slot '{}'".format(slot))
                if slot == "riddle_category":
                    message = "Quelle genre d'énigme aimes-tu ?\n"

                    dispatcher.utter_button_message(message, buttons)
                    return [SlotSet("requested_slot", slot)]

                if slot == "user_riddle_solution":
                    category = tracker.get_slot('riddle_category')

                    riddle_name, riddle, solution = get_riddle(enigma_df, category[0])

                    how_to_answer = "\n(Commence par \"Rep:\" puis écris ta réponse.)"

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
            message = f"Sans en être entièrement sûr, je crois que ta réponse est correcte.\
            \nLa bonne réponse est :\n{riddle_solution}"
        else:
            message = f"J'ai bien peur que cela soit une mauvaise réponse.\
            \nLa bonne réponse est :\n{riddle_solution}"

        dispatcher.utter_message(message)

        return [SlotSet("riddle_category", None), SlotSet("riddle_solution", None), SlotSet("user_riddle_solution", None)]

# class ActionCheckAnswer(Action):
#
#     def name(self) -> Text:
#         return "action_check_answer"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         solution = tracker.get_slot("riddle_solution")
#         solution_token =
#         # TODO : XXXXX
#
#         return []

# class NameForm(FormAction):
#     """Custom form action to fill user name slot."""
#
#     def name(self) -> Text:
#         """Unique identifier of the form"""
#
#         return "name_form"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#
#         return ["person"]
#
#     def slot_mappings(self) -> Dict[Text, Any]:
#         return {"person": self.from_entity(entity="person",
#                 intent=["user_introduces_himself"])}
#
#     def submit(self,
#                dispatcher: CollectingDispatcher,
#                tracker: Tracker,
#                domain: Dict[Text, Any]
#                ) -> List[Dict]:
#         """Once required slots are filled, print buttons for found facilities"""
#
#         name = tracker.get_slot('person')
#
#         message = f"Bonjour {name}."
#
#         # TODO: update rasa core version for configurable `button_type`
#         dispatcher.utter_message(message)
#
#         return []
