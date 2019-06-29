import json


class QueryPlatform(object):
    def __init__(self):
        self.data = self.initialize_data()

    @staticmethod
    def initialize_data():
        with open("data/platform_marketing.json", "r", encoding="utf-8") as f:
            data = json.load(f)['Platform']
            return data

    def get_by_names(self, names, sort_by=None, desc=True, top_k=5):
        tmp = []
        if isinstance(names, str):
            names = [names]
        for item in self.data:
            if item['name'] in names:
                tmp.append(item)
        if sort_by:
            tmp = sorted(tmp, key=lambda it: it[sort_by], reverse=desc)
        return tmp[0:top_k]

    def get_by_cost_range(self, min_cost, max_cost, sort_by=None, desc=True, top_k=5):
        tmp = []
        for item in self.data:
            if min_cost <= item['cost'] <= max_cost:
                tmp.append(item)
        if sort_by:
            tmp = sorted(tmp, key=lambda it: it[sort_by], reverse=desc)
        return tmp[:top_k]

    def get_by_types(self, types, sort_by=None, desc=True, top_k=5):
        tmp = []
        if isinstance(types, str):
            types = [types]
        for item in self.data:
            if item['type'] in types:
                tmp.append(item)
        if sort_by:
            tmp = sorted(tmp, key=lambda it: it[sort_by], reverse=desc)
        return tmp[0:top_k]

    def get_by_estimated_range(self, min_eta, max_eta, sort_by=None, desc=True, top_k=5):
        tmp = []
        for item in self.data:
            if min_eta <= item['estimated'] <= max_eta:
                tmp.append(item)
        if sort_by:
            tmp = sorted(tmp, key=lambda it: it[sort_by], reverse=desc)
        return tmp[:top_k]


if __name__ == "__main__":
    queryp = QueryPlatform()
    # res = queryp.data
    # res = queryp.get_by_names(['FaceBook', 'YouTube'], sort_by='estimated', desc=False)
    # res = queryp.get_by_cost_range(0, 1000, 'cost', False, 5)
    # res = queryp.get_by_types(['social', 'news'], sort_by='estimated', desc=False, top_k=None)
    res = queryp.get_by_estimated_range(200, 1000, sort_by='cost', desc=False, top_k=5)
    print(res)
