import credentials
import requests


class DataManager:

    def __init__(self):
        api_url = 'https://api.sheety.co/858d623b071a732795eb5ad26f9038d0/flightDeals/destinations'
        response = requests.get(url=api_url, headers=credentials.SHEETY)
        response.raise_for_status()
        self.data = response.json()


