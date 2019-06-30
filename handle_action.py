import json
import random
from query import query_investor, query_member
from send_mail import *
from query_answer import *

class HandleAction(object):
    def __init__(self, para):
        self.para = para
    
    @staticmethod
    def select_response(entity):
        with open("data/response.json", 'r') as f:
            response = json.load(f)
        response = response['response'][entity]
        return random.choice(response)

    @staticmethod
    def clear_str(text: str):
        return text.lower()

    def add_info(self):
        add_info_investor = query_investor.QueryInvestor()
        add_info_council = query_member.QueryMember()
        print(self.para)
        if self.para['rule'] == 'investor':
            print(type(self.para['name']))
            add_info_investor.add(f"{self.clear_str(self.para['name']['name'])}")
            add_info_investor.update_all_after_confirm()
            return "add done"
        elif self.para['rule'] == 'member':
            add_info_council.add(self.para['name']['name'])
            add_info_council.update_all_after_confirm()
            return "add done"

        # check lai
        elif self.para['rule'] == 'council':
            # add from csv a file
            return self.select_response("add_info") + f" {self.para['name']['name']}"

    def send_mail(self):

        if self.para["rule"] == "content":
            if self.para["email"]:
                return send_content("test", mail)
            else:
                if self.para["typeofperson"] == "member":
                    print(query_mail_btc())
                    return send_content("test", query_mail_btc())
                elif self.para["typeofperson"]:
                    return send_content("test", query_mail_investor())
                else:
                    return send_content("test", ["cheviethai123@gmail.com"])
        elif self.para["rule"]:
            if self.para["email"]:
                return send_invitation("test", mail)
            else:
                if self.para["typeofperson"]:
                    return send_invitation("test", query_mail_btc())
                elif self.para["typeofperson"]:
                    return send_invitation("test", query_mail_investor())
                else:
                    return send_invitation("test", ["cheviethai123@gmail.com"])
