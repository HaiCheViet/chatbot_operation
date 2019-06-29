import json

class QueryPlace(object):
    def __init__(self):
        self.data = self.initialize_data()

    @staticmethod
    def initialize_data():
        with open("data/place_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)['Place']
            return data
            
    def query_place(self, state, service=None, cost=None, capability=None, area=None):
        return_places = []
        for place in self.data:
            if place["location"]["state"] == state:
                return_places.append(place)
        
        return return_places

if __name__ == "__main__":
    query = QueryPlace()
    result = query.query_place("New York, United States")
    print(result)