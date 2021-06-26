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
            data = {'destinations': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}
            self.data = data['destinations']
            return self.data

    def update_row(self):
        for row in self.data:
            new_data = {
                "destination": {
                    "iataCode": row['iataCode']
                }
            }
            response = requests.put(
                url=f'{SHEETY_BASE_URL}/{row["id"]}',
                json=new_data,
                headers=credentials.SHEETY_HEADERS
            )
            response.raise_for_status()

