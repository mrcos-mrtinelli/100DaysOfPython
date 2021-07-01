import calendar

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials
from pprint import pprint

BILLBOARD_BASE_URL = 'https://www.billboard.com/charts/hot-100/'
SPOTIFY_BASE_URL = ''
is_correct_date = False

# Get user input
date_str = ""
songs = []

while not is_correct_date:
    try:
        date_str = input("Please enter a date in the format YYY-MM-DD: ")
        date_time_obj = datetime.strptime(date_str, '%Y-%m-%d')
        is_correct_date = True
        date_str = date_time_obj.strftime('%Y-%m-%d')
    except ValueError:
        print("Sorry, please enter the date in the correct format.\n")

res = requests.get(url=f'{BILLBOARD_BASE_URL}{date_str}')
soup = BeautifulSoup(res.text, 'html.parser')
li_elements = soup.find_all(name="li", class_="chart-list__element")

for el in li_elements:
    songs.append(
        {
            "rank": el.find(class_="chart-element__rank__number").string,
            "name": el.find(class_="chart-element__information__song").string,
            "artist": el.find(class_="chart-element__information__artist").string
        }
    )

scope = 'playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=credentials.SPOTIFY['app_id'],
    client_secret=credentials.SPOTIFY['app_secret'],
    redirect_uri='https://example.com',
    scope=scope
))
current_user_id = sp.current_user()['id']
song_uris = []
songs_not_found = []
year = date_str.split("-")[0]

for song in songs:
    search_q = f"track:{song['name']} year:{year}"
    res = sp.search(q=search_q, type="track")
    try:
        uri = res['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"\"{song['name']}\" not found and skipped from list.")
        songs_not_found.append(song)

playlist_res = sp.user_playlist_create(user=current_user_id, name=f"Top 100 as of {date_str}", public=False)
add_items_res = sp.playlist_add_items(playlist_id=playlist_res['id'], items=song_uris)

print("Done! Check your Spotify Playlist.")

