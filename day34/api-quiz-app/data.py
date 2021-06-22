import requests


def get_data():
    print("loading...")
    res = requests.get("https://opentdb.com/api.php",
                       params={"amount": 10,
                               "type": "boolean"
                               }
                       )
    res.raise_for_status()
    data = res.json()
    print("success")
    return data['results']


question_data = get_data()
