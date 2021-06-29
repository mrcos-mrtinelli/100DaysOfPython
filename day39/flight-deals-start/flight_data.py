class FlightData:

    def __init__(self, fly_from_code, fly_to_code, date_from, date_to, price_to):
        self.flight_type = "round"
        self.nights_in_dst_from = 6
        self.nights_in_dst_to = 27
        self.max_stopovers = 0
        self.curr = "GBP"
        self.price_to = price_to
        self.fly_from_code = fly_from_code
        self.fly_to_code = fly_to_code
        self.date_from = date_from
        self.date_to = date_to

    def get_params(self):
        params = {
            "fly_from": self.fly_from_code,
            "fly_to": self.fly_to_code,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "nights_in_dst_from": self.nights_in_dst_from,
            "nights_in_dst_to": self.nights_in_dst_to,
            "max_stopovers": self.max_stopovers,
            "flight_type": self.flight_type,
            "price_to": self.price_to,
            "curr": self.curr
        }
        return params
