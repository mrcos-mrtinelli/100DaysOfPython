class FlightSearch:

    def __init__(self):
        self.data = None

    def get_iata_code(self, city):
        if city['iataCode'] == "":
            city['iataCode'] = "TESTING"
            return city
