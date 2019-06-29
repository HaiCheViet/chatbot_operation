from pprint import pprint

import response
import query_answer
import switch_intent
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
    action = req.get('queryResult').get('action')
    intent = req.get('queryResult').get('intent')["displayName"]
    para = req.get('queryResult').get('parameters')

    fulfillment = response.fulfillment_response()
    Slack = response.SlackResponse()
    if action == 'setup':

        pass
    
    elif action == 'send_mail':
        '''
        @para:  typeofperson: [member, investor]
                rule: [content, appointment, reminder]
                (mail): mail
        '''
        if para['mail'] == '':
            # send mail to one person
            pass
        else:
            # send mail to a group
            pass

    elif action == 'add_info':
        '''
        @para:  rule: [member, investor]
                (name): name
        '''
        if para['name'] == '' and para['rule'] == 'member':
            # add member from csv file (get from google sheet)            
            pass
        elif para['name'] == '' and para['rule'] == 'investor':
            # request name of investor
            # response context  investor_follow
            pass
        elif para['name'] =! '' and para['rule'] == 'member':
            # request slot for member
            # response context member_follow
            pass
        else:
            # reply done
            pass

    elif action == 'add_info_investor':
        # add to database
        # reply done
        pass

    elif action == 'add_info_member':
        # add to database
        # reply done
        

        pass

    elif action == 'show_investor':
        from query.query_investor import QueryInvestor
        if para['rule'] == 'rank':
            # show investor by rank
            mess = query.query_investor_by_famous()
            
        elif para['rule'] == 'amount':
            # show investor by amount
            mess = query.query_investor_by_budget()
            
        elif para['rule'] == 'info' and para['organizer'] != '' :
            # show info investor
            mess = query.query_investor_by_name(para["organizer"])
            
        else:
            # reply: what do you want to show?
            mess = {}
    elif action == 'show_place':
        mess = query_answer.handle_mess_place()
    

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
