import credentials
import requests

SHEETY_BASE_URL = 'https://api.sheety.co/858d623b071a732795eb5ad26f9038d0/flightDeals/destinations'


class DataManager:

    def __init__(self):
        self.data = {}

    def get_data(self, live_request: bool = False):
        if live_request:
            response = requests.get(url=SHEETY_BASE_URL, headers=credentials.SHEETY_HEADERS)
            response.raise_for_status()
            data = response.json()
            self.data = data['destinations']
            return self.data
        else:
            data = {'destinations': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]}
            self.data = data['destinations']
            return self.data

    def update_rows(self, row_ids):
        for row_id in row_ids:
            for row in self.data:
                if row['id'] == row_id:
                    body = {
                        "destination": {
                            "iataCode": row['iataCode']
                        }
                    }
                    response = requests.put(
                        url=f'{SHEETY_BASE_URL}/{row["id"]}',
                        json=body,
                        headers=credentials.SHEETY_HEADERS
                    )
                    response.raise_for_status()

    def needs_update(self):
        for row in self.data:
            if row['iataCode'] == "":
                return True
        return False
