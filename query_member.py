import json
class QueryMember(object):
    def __init__(self):
        self.data = self.initialize_data()
    
    @staticmethod
    def initialize_data():
        with open("data/member_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)['Member']
            return data
    def query_member(self,name, position=None):
        '''input :query by condition 
           return : name member '''
        name_member = []
        for i in range(len(self.data)):
            if self.data[i]["name"].lower() == name :
                name_member.append(self.data[i])
        return name_member
if __name__ == "__main__":
    query =  QueryMember()
    name_member = query.query_member("sharon w. tierney")
    print(name_member)

