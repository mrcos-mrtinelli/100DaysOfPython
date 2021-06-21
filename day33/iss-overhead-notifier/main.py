import time
from datetime import datetime
import requests
import smtplib

# CONSTANTS
ISS_API_URL = "http://api.open-notify.org/iss-now.json"
SUNSET_RISE_API_URL = "https://api.sunrise-sunset.org/json"
MY_COORD = {
    "lat": 33.608768,
    "lng": -117.873360
}


def get_json(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def is_visible(sunset, sunrise):
    if sunset < current_time < sunrise:
        return True
    return False


def is_in_range(my_coord, iss_coord):
    my_lat1 = my_coord['lat'] - 5
    my_lat2 = my_coord['lat'] + 5
    my_lng1 = my_coord['lng'] - 5
    my_lng2 = my_coord['lng'] + 5

    if my_lat1 <= iss_coord['lat'] <= my_lat2:
        if my_lng1 <= iss_coord['lng'] <= my_lng2:
            return True
    return False


current_time = datetime.now().isoformat()

iss_data = get_json(url=ISS_API_URL)
iss_lat = iss_data['iss_position']['latitude']
iss_long = iss_data['iss_position']['longitude']
iss_coord = {
    'lat': float(iss_lat),
    'lng': float(iss_long)
}

sunset_rise_data = get_json(
    url=SUNSET_RISE_API_URL,
    params={
        "lat": MY_COORD['lat'],
        "lng": MY_COORD['lng'],
        "formatted": 0
    }
)
sunrise = sunset_rise_data['results']['sunrise']
sunset = sunset_rise_data['results']['sunset']

while True:
    time.sleep(60)
    if is_in_range(MY_COORD, iss_coord) and is_visible(sunset, sunrise):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user='', password='')
            connection.send_message("Subject:Look to the Sky!\n\nThe ISS is passing by, wave 👋🏼")


