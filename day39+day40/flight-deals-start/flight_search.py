import requests
import credentials
from flight_data import FlightData

TEQUILA_BASE_URL = 'https://tequila-api.kiwi.com'


class FlightSearch:

    def __init__(self):
        self.data = None
        self.flight_query = None

    def get_iata_code(self, city):
        params = {
            "term": city
        }
        r = requests.get(
            url=f"{TEQUILA_BASE_URL}/locations/query/",
            params=params,
            headers=credentials.TEQUILA_HEADERS
        )
        r.raise_for_status()
        self.data = r.json()
        return self.data['locations'][0]['code']

    def get_flights(self):
        r = requests.get(
            url=f'{TEQUILA_BASE_URL}/v2/search',
            params=self.flight_query,
            headers=credentials.TEQUILA_HEADERS
        )
        r.raise_for_status()
        flights = r.json()['data']

        if len(flights) > 0 and flights[0] is not None:
            return flights[0]
        else:
            print(f"No flights available to {self.flight_query['fly_to']} "
                  f"at max price of {self.flight_query['price_to']}")
            return None
