from datetime import datetime
import requests



# CONSTANTS
ISS_API_URL = "http://api.open-notify.org/iss-now.json"
SUNSET_RISE_API_URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 33.608768
MY_LONG = -117.873360
current_time = datetime.now().isoformat()


# 33.598753361993815, -117.89499841466444
def get_json(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


iss_data = get_json(url=ISS_API_URL)
iss_lat = iss_data['iss_position']['latitude']
iss_long = iss_data['iss_position']['longitude']

sunset_rise_data = get_json(url=SUNSET_RISE_API_URL, params={"lat": MY_LAT, "lng": MY_LONG, "formatted": 0})
sunrise = sunset_rise_data['results']['sunrise']
sunset = sunset_rise_data['results']['sunset']


