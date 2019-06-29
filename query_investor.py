import json
class QueryInvestor(object):
    def __init__(self):
        self.data = self.initialize_data()
    
    @staticmethod
    def initialize_data():
        with open("data/investor_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)['Investor']
            return data
    def query_investor(self,name, budget_history=None, famous_ratio=None):
        '''input :query by condition budget or famous ratio
           return : name investor '''
        name_investor = []
        for i in range(len(self.data)):
            if self.data[i]["name"].lower() == name :
                name_investor.append(self.data[i])
        return name_investor
if __name__ == "__main__":
    query =  QueryInvestor()
    name_investor = query.query_investor("modern realty")
    print(name_investor)

