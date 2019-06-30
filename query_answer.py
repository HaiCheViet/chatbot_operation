from query.query_investor import QueryInvestor
from query.query_place import QueryPlace
from query.query_member import QueryMember

def handle_mess_invest(para):
    query = QueryInvestor()
    if para["query_investor"] == "info":
        return query.query_investor_by_name(para["organizer"])
    elif para["query_investor"] == "amount":
        return query.query_investor_by_budget()
    elif para["query_investor"] == "rank":
        return query.query_investor_by_famous()
    else:
        return "Entity was not defined"

def handle_mess_place(para):
    query = QueryPlace()
    if para["rule"] == "space":
        return query.query_place_by_state(para["location"], capability=True)
    elif para["rule"] == "cost":
        return query.query_place_by_state(para["location"], cost=True)
    else:
        return query.query_place_by_state(para["location"])

def query_mail_investor():
    query = QueryInvestor()
    return query.query_investor_by_email()

def query_mail_btc():
    query = QueryMember()
    return query.query_member_by_email()