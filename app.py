from pprint import pprint

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
log = app.logger

list_sequence = []


@app.route('/home')
def home():
    return make_response(jsonify('Hello, Nice to meet you!'))


@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    # build request object
    req = request.get_json(force=True)
    # get action from json
    # action = req.get('queryResult').get('action')
    intent = req.get('queryResult').get('intent')["displayName"]
    # intent = req.get('intent').get('query_investor_intent')
    # print(req)
    pprint(req)
    print(intent)

    list_sequence.append(intent)
    if intent == "query_investor_intent"
        return

    resp = {"fulfillmentText": "hello"}
    return make_response(jsonify(resp))
    # print(intent)


if __name__ == "__main__":
    app.run(port=6789)
