        # This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
import numpy as np

class ActionQuelJeu(Action):

    def name(self) -> Text:
        return "action_quel_jeu"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        which_game = "Par quel jeu es-tu intéressé ?"
        game_1 = "La Société Mystérieuse de Strasbourg"
        game_2 = "1913, Meurte à la Krutenau"

        buttons = [{"title": game_1, "payload": game_1},
            {"title": game_2, "payload": game_2}]

        dispatcher.utter_button_message(which_game, buttons)

        return []

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        m1 = "Je ne suis pas sûr de comprendre, pourrais-tu reformuler ?"
        m2 = "Je suis désolé, je n'ai pas compris. Est-il possible de reformuler la requête ?"
        m3 = "Excuse-moi mais je n'ai pas compris ce que tu demandes, est-ce que tu pourrais reformuler ?"

        message = np.random.choice(np.array([m1, m2, m3]))

        dispatcher.utter_message(message)

        return []

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
