# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionSavename(Action):
    def name(self) -> Text:
        return "action_save_name"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entity_name = tracker.latest_message.get("entities", [])
        # Save the username or perform any other necessary processing

        if entity_name:
            name = entity_name[0].get("value")
        else:
            name = None  # Handle the case when no entity is present

        return [SlotSet("name", name)]


class ActionBeingLost(Action):
    def name(self) -> Text:
        return "action_being_lost"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entity_love_one = tracker.latest_message.get("entities", [])
        # Save the username or perform any other necessary processing

        if entity_love_one:
            loved_one = entity_love_one[0].get("value")
        else:
            loved_one = None  # Handle the case when no entity is present

        return [SlotSet("loved_one", loved_one)]
