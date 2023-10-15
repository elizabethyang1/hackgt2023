import csv
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Load FAQs from CSV
FAQ = {}

with open('faq.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        FAQ[row[0]] = row[1]


class ActionRetrieveFAQ(Action):

    def name(self) -> Text:
        return "action_retrieve_faq"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the intent from the tracker
        intent = tracker.latest_message['intent'].get('name')
        faq_response = None

        # Map intents to FAQ questions
        if intent == 'ask_personal_finance':
            faq_response = FAQ["What is personal finance?"]
        elif intent == 'ask_create_budget':
            faq_response = FAQ["How can I create a budget?"]
        elif intent == 'ask_types_of_insurance':
            faq_response = FAQ["What are the different types of insurance?"]
        elif intent == 'ask_credit_score':
            faq_response = FAQ["How is a credit score calculated?"]
        elif intent == 'ask_investment_strategies':
            faq_response = FAQ["What are some investment strategies?"]
        elif intent == 'ask_tax_filing':
            faq_response = FAQ["How do I file my taxes?"]
        elif intent == 'ask_retirement_planning':
            faq_response = FAQ["How do I plan for retirement?"]
        elif intent == 'ask_savings_tips':
            faq_response = FAQ["What are some tips for saving money?"]
        else:
            faq_response = "I'm sorry, I don't have information for that question."

        dispatcher.utter_message(text=faq_response)

        return []
