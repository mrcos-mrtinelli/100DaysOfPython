import requests
import smtplib


# CONSTANT
API_KEY = '45facd356f717d510e657efac40df4cd'
BASE_URL = 'https://api.openweathermap.org/data/2.5/onecall'
LAT = 25.115568712991706
LON = 121.54844826750485
# 25.115568712991706, 121.54844826750485
# 33.615606142433535, -117.87549298722794


def get_weather_data(base, key, lat, lon):
    data = requests.get(base, params={
        "appid": key,
        "lat": lat,
        "lon": lon,
        "units": "imperial",
        "exclude": "current,minutely,daily,alerts"
    })
    weather_json = data.json()
    return weather_json['hourly']


def get_rain(all_weather):
    is_rain = False
    for w in all_weather[:12]:
        if w['weather'][0]['id'] < 700:
            is_rain = True
    if is_rain:
        send_rain_alert()


def send_rain_alert():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user='', password='')
        connection.sendmail(from_addr='email@email.com',
                            to_addrs='email@email.com',
                            msg="Subject:Bring and Umbrella!\n\nIt's going to rain today."
                            )


hourly_weather = get_weather_data(BASE_URL, API_KEY, LAT, LON)
get_rain(hourly_weather)


