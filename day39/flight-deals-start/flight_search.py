import requests
import credentials

TEQUILA_BASE_URL = 'https://tequila-api.kiwi.com'


class FlightSearch:

    def __init__(self):
        self.data = None

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

