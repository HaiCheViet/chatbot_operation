import json
from random import shuffle

from query_answer import *


class HandleIntent(object):
    def __init__(self, intent, para):
        self.intent = intent
        self.para = para
    @staticmethod
    def select_response(entity):
        with open("response.json", 'r') as f:
            response = json.load(f)
        response = response['response'][entity]
        shuffle(response)
        return response[0] + "\n"

    def handle_info(self):
        return self.select_response("add_info") + f" {self.para['name']}"

    # def sent_mail(self):

    def switch_intent(self):
        if self.intent == "query_investor_intent":
            return handle_mess_invest()
        elif self.intent == "add_info":
            return self.handle_info()
        elif self.intent == ""
