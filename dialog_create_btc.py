class BtcRequest(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.event_name = None
        self.btc = None
        self.investor = None
        self.start_date = None
        self.end_date = None
        self.list_place = None

    def get_any_null_item(self):
        temp = []
        if self.event_name is None:
            temp.append("Tên ")
        if self.btc is None:
            temp.append("Số điện thoại")
        if self.investor is None:
            temp.append("Kinh phí")
        if self.start_date is None:
            temp.append("Nơi đang ở")
        if self.end_date is None:
            temp.append("Nơi đến")
        if self.str_date is None:
            temp.append("Ngày đi")

        return temp

    def update_all_information(self, var):
        for key, value in var.items():
            setattr(self, key, value)

    @property
    def get_user_request(self):
        result = {
            "event_name": self.event_name,
            "btc": self.btc,
            "investor": self.investor,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "list_place": self.list_place
        }
        return json.dumps(result)

    @property
    def get_str_date(self):
        return self.list_place
    
    @property
    def get_place(self):
        return self.start_date, self.end_date
    
    @property
    def get_budget(self):
        return self.investor

    def send_request(self, flight_data):
        result = {}
        with io.open("request/request.json", 'w', encoding='utf-8') as f:
            result.update(self.get_all_information())
            result.update(flight_data.get_result[0])
            json.dump(result, f, ensure_ascii=False)

    def handle_message(response, data, )