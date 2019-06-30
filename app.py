from pprint import pprint

import json
import random
import response
import query_answer
from switch_intent import HandleIntent
from flask import Flask, request, make_response, jsonify
from query.query_investor import QueryInvestor

import handle_action

app = Flask(__name__)
log = app.logger

list_sequence = []


@app.route('/home')
def home():
    return make_response(jsonify('Hello, Nice to meet you!'))

def recommend_operation(list_sequence):
    list_of_recommend_task = []
    if len(list_sequence) == 1:
        return []
    with open("data/recommend.json", "r") as f:
        recommend = json.load(f)
    # print(recommend)
    for k in recommend.keys():
        if list_sequence == recommend[k][0:len(list_sequence)]:
            if len(list_sequence) == len(recommend[k]):
                return f"Finish sequence {recommend[k]}"

            list_of_recommend_task.append({k: recommend[k][len(list_sequence)]})
    return list_of_recommend_task


@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    # build request object
    req = request.get_json(force=True)
    # get action from json
    action = req.get('queryResult').get('action')
    # intent = req.get('queryResult').get('intent')["displayName"]
    para = req.get('queryResult').get('parameters')
    list_sequence.append(action)

    # fulfillment = response.fulfillment_response()
    slack = response.SlackResponse()

    list_recommend_task = recommend_operation(list_sequence)

    handle = handle_action.HandleAction(para)
    if action == 'setup':
        text = 'Hi! Can I help you? \n You can follow one of these operations'
        button = slack.message_buttons(["send mail to council group", 'add info', "sent mail appointment to council group"])
        seq = slack.recommend_seq(list_recommend_task)

        reply = slack.response(text, button, seq)
    
    elif action == 'send_mail':
        '''
        @para:  typeofperson: [member, investor, council]
                rule: [content, appointment, reminder]
                (mail): mail
        '''
        # handle_intent = HandleIntent(intent, para)
        # if para['rule'] == 'content':
        #     if para['typeofperson'] == 'council':
        #         # send mail to a person or people of member group
        #         result = handle.send_mail(rule=para['content'], 
        #                         typeofperson=para['typeofperson'], mail=para['mail'])
        #         if result:
        #             text = handle.select_response('send_mail')
        #             reply = slack.text_response(text)
        #         else: reply = slack.text_response("I missed it")

        #     elif para['typeofperson'] == 'investor':
        #         # send mail to a person or people of member group
        result = handle.send_mail()
        if result:
            text = handle.select_response('send_mail')
            seq = slack.recommend_seq(list_recommend_task)
            reply = slack.response(text, seq=seq)
            print(reply)

        else: reply = slack.text_response("Sorry, I missed it")
                       

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
        seq = slack.recommend_seq(list_recommend_task)
        reply = slack.response(text, seq=seq)

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
            text = investor.query_investor_by_famous()
            seq = slack.recommend_seq(list_recommend_task)
            reply = slack.response(text, seq=seq)
            
        elif para['rule'] == 'amount':
            # show investor by amount
            text = investor.query_investor_by_budget()
            seq = slack.recommend_seq(list_recommend_task)
            reply = slack.response(text, seq=seq)
            
        elif para['rule'] == 'info' and para['organizer'] != '' :
            # show info investor
            text = investor.query_investor_by_name(para["organizer"])
            seq = slack.recommend_seq(list_recommend_task)
            reply = slack.response(text, seq=seq)
            
        else:
            # reply: what do you want to show?
            reply = "sorry"
    elif action == 'show_place':
        text = query_answer.handle_mess_place(para)
        seq = slack.recommend_seq(list_recommend_task)
        reply = slack.response(text, seq=seq)
        # reply = slack.text_response(str(text))

        
    
    

    # pprint(reply)
    return make_response(jsonify(reply))
    # print(intent)



if __name__ == "__main__":
    app.run(port=6789)
