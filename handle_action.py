import json
import random 

class HandleAction(object):
    def __init__(self, para):
        self.para = para
    
    @staticmethod
    def select_response(entity):
        with open("data/response.json", 'r') as f:
            response = json.load(f)
        response = response['response'][entity]
        return random.choice(response)

    def add_info(self):
        if para[]
        return self.select_response("add_info") + f" {self.para['name']}"