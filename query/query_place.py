import json

class QueryPlace(object):
    def __init__(self):
        self.data = self.initialize_data()

    @staticmethod
    def initialize_data():
        with open("data/place_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)['Place']
            return data

    def query_place_info_by_name(self, name):
        for place in self.data:
            if place["name"] = name:
                return place

    def query_place_email_by_name(self, name):
        for place in self.data:
            if place["name"] == name:
                return place["email"]
            
    def query_place_by_state(self, state: str, cost=False, capability=False):
        temp_return_places = []
        return_places = []
        for place in self.data:
            if place["location"]["state"] == state:
                temp_return_places.append(place)
        if cost:
            temp_return_places = sorted(temp_return_places, key=lambda x: x["cost"])[:3]
        if capability:
            temp_return_places = sorted(temp_return_places, key=lambda x: x["capability"], reverse=True)[:3]
        
        for place in temp_return_places:
            return_places.append(place["name"])

        return return_places

    def query_place_by_service(self, service: float):
        return_places = []
        for place in self.data:
            if place["service"] >= service:
                return_places.append(place)
        return sorted(return_places, key=lambda x: x["service"], reverse=True)[:3]

    def query_place_by_cost(self, cost: int):
        return_places = []
        for place in self.data:
            if place["cost"] <= cost:
                return_places.append(place)
        return sorted(return_places, key=lambda x: x["cost"])[:3]

    def query_place_by_capability(self, capability: int):
        return_places = []
        for place in self.data:
            if place["capability"] >= capability:
                return_places.append(place)
        return sorted(return_places, key=lambda x: x["capability"], reverse=True)[:3]

    def query_place_by_area(self, area: int):
        return_places = []
        for place in self.data:
            if place["area"] >= area:
                return_places.append(place)
        return sorted(return_places, key=lambda x: x["area"], reverse=True)[:3]

if __name__ == "__main__":
    query = QueryPlace()
    result = query.query_place_state("New York, United States", cost=True)
    # result = query.query_place_cost(1500)
    print(result)