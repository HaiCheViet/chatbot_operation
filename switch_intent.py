import json
from random import shuffle

from query_answer import *
from send_mail import *


class HandleIntent(object):
    def __init__(self, intent, para):
        self.intent = intent
        self.para = para
    @staticmethod
    def select_response(entity):
        with open("data/response.json", 'r') as f:
            response = json.load(f)
        response = response['response'][entity]
        shuffle(response)
        return response[0] + "\n"

    def handle_info(self):
        if self.intent == ""
        return self.select_response("add_info") + f" {self.para['name']}"

    # def sent_mail(self):

    def switch_intent(self):
        if self.intent == "query_investor_intent":
            return handle_mess_invest()
        elif self.intent == "add_info":
            return self.handle_info()
        elif self.intent == "send_email":
            if self.para["rule"] == "content":
                if self.para["rule"] == "member":
                    return send_content("test", ["cheviethai123@gmail.com"])
                elif self.para["rule"] == "investor":
                    return send_content("test", handle_mess_invest(self.para))
            elif self.para["rule"] == "appointment":
                if self.para["rule"] == "member":
                    send_invitation("test", ["cheviethai123@gmail.com"])
                elif self.para["rule"] == "investor":
                    return send_invitation("test", handle_mess_invest(self.para))

            else:
                return "haven't develop"

