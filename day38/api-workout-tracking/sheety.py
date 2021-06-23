import credentials as cr
from datetime import datetime
import requests

_BASE_URL = 'https://api.sheety.co/858d623b071a732795eb5ad26f9038d0/myApiWorkout/sheet1'
_HEADER = {
    "Authorization": cr.SHEETY['Authorization'],
    "Content-Type": "application/json"
}


class Sheety:

    def __init__(self, exercises):
        self.exercises = exercises
        self.date = datetime.now().strftime('%m/%d/%Y')
        self.time = datetime.now().strftime('%H:%M:%S')

    def post_to_sheets(self):
        for exercise in self.exercises:
            body = {
                "sheet1": {
                    "date": self.date,
                    "time": self.time,
                    "exercise": exercise['name'],
                    "duration": exercise['duration_min'],
                    "calories": exercise['nf_calories']
                }
            }
            print(body)
            request = requests.post(url=_BASE_URL, json=body, headers=_HEADER)
            request.raise_for_status()
            print(request.status_code)
