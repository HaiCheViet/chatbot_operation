import json
class QueryMember(object):
    def __init__(self):
        self.data = self.initialize_data()
    
    @staticmethod
    def initialize_data():
        with open("./data/member_database.json", "r", encoding="utf-8") as f:
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
    
    def query_member_by_email(self):
        email_member = []
        for i in range(len(self.data)):
            email_member.append(self.data[i]["email"])
        return  email_member
    def query_member_join(self):
        member_join = []
        for i in range(len(self.data)):
            if self.data[i]["is_join"]:
                member_join.append(self.data[i])
        return member_join

    def add(self,name):
        for i in range(len(self.data)):
            if self.data[i]["name"].lower() == name:
                self.data[i]["is_join"] = True
    
    def update_all_after_confirm(self):
        with open("./data/member_database.json", "w", encoding="utf-8") as f:
           json.dump(self.data, f)
if __name__ == "__main__":
    query =  QueryMember()
    query.update_all_after_confirm()
    query.add("edna s. hille")
    name_member = query.query_member_join()
    print(name_member)

