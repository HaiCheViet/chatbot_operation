import json
class QueryCouncil(object):
    def __init__(self):
        self.data = self.initialize_data()
    
    @staticmethod
    def initialize_data():
        with open("data/council_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)['Council']
            return data
    def query_council(self,name, position=None):
        '''input :query by condition 
           return : name council '''
        name_council = []
        for i in range(len(self.data)):
            if self.data[i]["name"].lower() == name :
                name_council.append(self.data[i])
        return name_council
if __name__ == "__main__":
    query =  QueryCouncil()
    name_council = query.query_council("sharon w. tierney")
    print(name_council)

