import requests


BASE_URL = "https://trackapi.nutritionix.com"
HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

endpoint = "/v2/natural/exercise"
full_url = f"{BASE_URL}{endpoint}"
json_query = {"query":input("Enter your exercise: ")}

response = requests.post(url=full_url,json=json_query, headers=HEADER)
response.raise_for_status()
print(response.text)

