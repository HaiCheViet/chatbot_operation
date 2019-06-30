from pprint import pprint

import response
import query_answer
import switch_intent
from flask import Flask, request, make_response, jsonify
from query.query_investor import QueryInvestor

import handle_action

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
    slack = response.SlackResponse()

    handle = handle_action.HandleAction(para)
    if action == 'setup':
        text = 'Hi! Can I help you ?'
        button = ['setup', 'send mail', 'add info', 'show place']
        reply = slack.message_buttons(text, button)
    
    elif action == 'send_mail':
        '''
        @para:  typeofperson: [member, investor]
                rule: [content, appointment, reminder]
                (mail): mail
        '''
        if para['mail'] != '':
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
        # if para['name'] == '' and para['rule'] == 'member':
        #     # add member from csv file (get from google sheet)         
        #     pass
        # elif para['name'] == '' and para['rule'] == 'investor':
        #     # request name of investor
        #     # response context  investor_follow
        #     pass
        # elif para['name'] != '' and para['rule'] == 'member':
        #     # request slot for member
        #     # response context member_follow
        #     pass
        # else:
        #     # reply done
        #     pass
        text = handle.add_info()
        reply = slack.text_response(text)

    # elif action == 'add_info_investor':
    #     # add to database
    #     # reply done
    #     pass

    # elif action == 'add_info_member':
    #     # add to database
    #     # reply done
        

    #     pass

    elif action == 'show_investor':
        investor = QueryInvestor()
        if para['rule'] == 'rank':
            # show investor by rank
            reply = investor.query_investor_by_famous()
            
        elif para['rule'] == 'amount':
            # show investor by amount
            reply = investor.query_investor_by_budget()
            
        elif para['rule'] == 'info' and para['organizer'] != '' :
            # show info investor
            reply = investor.query_investor_by_name(para["organizer"])
            
        else:
            # reply: what do you want to show?
            reply = "sorry"
    elif action == 'show_place':
        reply = query_answer.handle_mess_place()
    

    # pprint(req)
    # print(intent)


    # pprint(reply)
    return make_response(jsonify(reply))
    # print(intent)


if __name__ == "__main__":
    app.run(port=6789)
