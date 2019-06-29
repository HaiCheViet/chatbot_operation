import json


class QueryInvestor(object):
    def __init__(self):
        self.data = self.initialize_data()
    
    @staticmethod
    def initialize_data():
        with open("data/investor_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)['Investor']
            return data
    def query_investor_by_name(self,name):
        '''input :query by condition budget or famous ratio
           return : name investor '''
        name_investor = []
        for i in range(len(self.data)):
            if self.data[i]["name"].lower() == name :
                name_investor.append(self.data[i])
        return name_investor


    

    def query_investor_by_budget(self):
        '''input :query by condition budget or famous ratio
           return : name investor '''
        def sum_bugdet(investor):
            return sum([his['budget'] for his in investor['history_investment']])
        # name_investor = []

        # for i in range(len(self.data)):
        return sorted(self.data, key=lambda invt: sum_bugdet(invt), reverse=True)[:3]

    def query_investor_by_famous(self):

        return sorted(self.data, key=lambda invt: invt['famous_ratio'], reverse=True)[:3]
        
if __name__ == "__main__":
    query =  QueryInvestor()
    # name_investor = query.query_investor("modern realty")
    name_investor = query.query_investor_by_famous()
    print(name_investor)

