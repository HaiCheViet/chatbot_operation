from query.query_investor import QueryInvestor

def handle_mess_invest(para):
    query = QueryInvestor()
    if para["query_investor"] == "info":
        query.query_investor_name(para["organizer"])
    elif para["query_investor"] == "amount":
        query.query_investor_budge()
    elif para["query_investor"] == "rank":
        query.query_investor_rank()
    else:
        return "Entity was not defined"

def handle_mess_place(para):
