# Develop complex shortcuts for a Spotify user
# Example: shortcut to play a song from the Liked Songs playlist
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import json
import os
'''
scope = "user-library-read"
CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
REDIRECT = os.environ.get('SPOTIPY_REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
'''

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID') # '18b3ecc0df694ca7aa9a0127e07e3531'
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET') #'e284a47688ce45a6917e93b753c86b50'

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

# '6mFkJmJqdDVQ1REhVfGgd1'

BASE_URL = 'https://api.spotify.com/v1/'
# track_id = input('Enter track id: ')
beyonce_id = '6vWDO969PvNqNYHIOW5v0m'
# r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
artist = requests.get(BASE_URL + 'artists/' + beyonce_id, headers=headers)
artist_albums = requests.get(BASE_URL + 'artists/' + beyonce_id + '/albums', headers=headers)

artist_data = artist.json()
album_data = artist_albums.json()

# print(artist_data)
# Print out all the album releases made by the artist.
for i in range(len(album_data['items'])):
  print(album_data['items'][i]['name'])

