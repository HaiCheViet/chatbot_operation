from query.query_investor import QueryInvestor
from query.query_place import QueryPlace

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
        return query.query_place_state(para["location"], capability=True)
    elif para["rule"] == "cost":
        return query.query_place_state(para["location"], cost=True)