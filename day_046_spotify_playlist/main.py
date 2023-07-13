# Ask user for a date, find the hot 100 songs on Billboard for that date
# then create a new list and all songs that could be found to it
# SKILLS: web scraping, API
# Difficulty: hard (too many bumps with Spotipy and Spotify API)

import os
import re
import requests
from bs4 import BeautifulSoup
from spotify_info import client_id, client_secret
import spotipy
from spotipy.oauth2 import SpotifyOAuth

os.environ['SPOTIPY_CLIENT_ID'] = client_id
os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://example.org/'

# ===Get the hot 100 songs from a past point
date_regex = r"\d{4}-\d{2}-\d{2}"
format_is_ok = False
while not format_is_ok:
    date_to_go = input("What date do you want to go back to? Please input in format yyyy-mm-dd:\n")
    format_is_ok = re.search(date_regex, date_to_go)
    if format_is_ok and len(date_to_go) == 10:
        print(f'Going back to {date_to_go}')
    else:
        print("Sorry, I cannot recognise the date, please input again.")
url = f"https://www.billboard.com/charts/hot-100/{date_to_go}/"
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
# ===Extract song names and artists===
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
artists_uncleaned = soup.select('li ul li span')
artists_uncleaned = [artist.getText().strip() for artist in artists_uncleaned]
artists: list = []
for artist in artists_uncleaned:
    if artist.isdigit():
        continue
    elif artist == '-':
        continue
    else:
        artists.append(artist)
song_artist = []
for i in range(len(artists)):
    song_artist.append([song_names[i], artists[i]])
print(song_artist)

# Spotify authentication
scope = 'playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Find all songs' URIs
song_uris = []
for song in song_artist:
    print(f'Processing {song}')
    result = sp.search(q=f'track:{song[0]} artist:{song[1]}', type='track')
    # print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
        print(f'\n{song} added\n')
    except Exception as E:
        print(f'Error: {song} {E}')
print(f'\nFound {len(song_uris)} songs in total\n')

# user_id = '314qxemcswpzo5oalmmizrzd52yi'
user_id = sp.current_user()['id']

# raise SystemExit(0)
playlist_info = sp.user_playlist_create(
    user=user_id,
    name=f'Hot 100 Songs on {date_to_go}',
    public=False,
    description=f'The top 100 songs in the week of {date_to_go} according to Billboard'
)
sp.playlist_add_items(playlist_id=playlist_info['id'], items=song_uris)
print('All found songs added to playlist!')
