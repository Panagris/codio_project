# Develop complex shortcuts for a Spotify user
# Example: shortcut to play a song from the Liked Songs playlist
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth

# use source ~/.bashrc to load environment variables
import requests
import json
import os
import pandas as pd
import sqlalchemy as db
from sqlalchemy.types import TEXT

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

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
# print(auth_response_data)


access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

# '6mFkJmJqdDVQ1REhVfGgd1'

BASE_URL = 'https://api.spotify.com/v1/'
# track_id = input('Enter track id: ')
beyonce_id = '6vWDO969PvNqNYHIOW5v0m'
# r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
artist = requests.get(BASE_URL + 'artists/' + beyonce_id, headers=headers)
artist_albums = requests.get(BASE_URL + 'artists/' +
                             beyonce_id + '/albums', headers=headers)

artist_data = artist.json()
album_data = artist_albums.json()

# Print out all the album releases made by the artist.

# Unpack the JSON data into the form {field : array-like} to allow pandas
# and SQL to work effectively.
new_dict = {"Albums": []}

for i in range(len(album_data['items'])):
    new_dict["Albums"].append(album_data['items'][i]['name'])

# Create an engine object to make a path for a database.
engine = db.create_engine('sqlite:///artist_info.db')
# Create a data frame from the unpacked JSON data dictionary.
df = pd.DataFrame.from_dict(new_dict)

# Convert the data frame to SQL.
df.to_sql('artist', con=engine, if_exists='replace', index=False,
          dtype={"A": TEXT()})

with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM artist;")
                                      ).fetchall()
    print(pd.DataFrame(query_result))
