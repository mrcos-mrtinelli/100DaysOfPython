from bs4 import BeautifulSoup
from datetime import datetime
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials


BASE_URL = 'https://www.billboard.com/charts/hot-100/'
is_correct_date = False

# Get user input
date_str = ""
songs = []

# while not is_correct_date:
#     try:
#         date_str = input("Please enter a date in the format YYY-MM-DD: ")
#         date_time_obj = datetime.strptime(date_str, '%Y-%m-%d')
#         is_correct_date = True
#         date_str = date_time_obj.strftime('%Y-%m-%d')
#     except ValueError:
#         print("Sorry, please enter the date in the correct format.\n")
#
# res = requests.get(url=f'{BASE_URL}{date_str}')
# soup = BeautifulSoup(res.text, 'html.parser')
# li_elements = soup.find_all(name="li", class_="chart-list__element")
#
# for el in li_elements:
#     songs.append(
#         {
#             "rank": el.find(class_="chart-element__rank__number").string,
#             "song": el.find(class_="chart-element__information__song").string,
#             "artist": el.find(class_="chart-element__information__artist").string
#         }
#     )

scope = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=credentials.SPOTIFY['app_id'],
    client_secret=credentials.SPOTIFY['app_secret'],
    redirect_uri='https://example.com',
    scope=scope
))

current_user = sp.current_user()
print(current_user['id'])
