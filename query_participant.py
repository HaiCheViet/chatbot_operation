import json

class QueryParticipant(object):
    def __init__(self):
        self.template = self.initialize_template()
        self.data = self.initialize_data()

    @staticmethod
    def initialize_template():
        with open("data/participant_template.json", "r", encoding="utf-8") as f:
            template = json.load(f)
            return template

    @staticmethod
    def initialize_data():
        with open("data/participant_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    # def query_place(self, state, service=None, cost=None, capability=None, area=None):
    #     return_places = []
    #     for place in self.data:
    #         if place["location"]["state"] == state:
    #             return_places.append(place)
        
    #     return return_places
    def add_participant(self, name, job, experience_years,
                        birth_year, channel, address, phone,
                        email, confirm=False):
        if self.data == []:
            self.template["id"] = 1
        else:
            if email in [p["email"] for p in self.data["Participant"]]:
                print("Participant exists !!!")
                return
            else:
                self.template["id"] = len(self.data["Participant"]) + 1
        self.template["name"] = name
        self.template["job"] = job
        self.template["experience years"] = experience_years
        self.template["birth year"] = birth_year
        self.template["channel"] = channel
        self.template["address"] = address
        self.template["phone"] = phone
        self.template["email"] = email
        self.data["Participant"].append(self.template)
        with open("data/participant_database.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f)

        return

    def set_confirm(self, email):
        for i in range(len(self.data["Participant"])):
            if self.data["Participant"][i]["email"] == email:
                self.data["Participant"][i]["confirm"] = True
        pass

    def update_all_after_confirm(self):
        with open("data/participant_database.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f)

if __name__ == "__main__":
    query = QueryParticipant()

    # Add participant
    query.add_participant("Donald J. Hardin", "Business Analysis", 3, 1992, "facebook", "437 Braxton Street", "815-485-4433", "DonaldJHardin@jourrapide.com")

    # Confirm participate
    # list_of_confirm = ["DonaldJHardin@jourrapide.com"]
    # for email in list_of_confirm:
    #     query.set_confirm(email)
    # query.update_all_after_confirm()