import credentials as cr
import requests

_BASE_URL = "https://trackapi.nutritionix.com"
_HEADER = {
    "x-app-id": cr.NUTRITIONIX['APP_ID'],
    "x-app-key": cr.NUTRITIONIX['APP_KEY']
}

class NutritionIX:

    def __init__(self, query):
        self.query = query
        self.exercise_data = self.get_exercise_data()

    def get_exercise_data(self):
        endpoint = '/v2/natural/exercise'
        json_query = {"query": self.query}
        response = requests.post(url=f'{_BASE_URL}{endpoint}', json=json_query, headers=_HEADER)
        response.raise_for_status()
        return response.json()

