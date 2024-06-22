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

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
AUTH_URL = 'https://accounts.spotify.com/api/token'


def issue_HTTP_request() -> dict:
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

    BASE_URL = 'https://api.spotify.com/v1/'
    # track_id = input('Enter track id: ')
    beyonce_id = '6vWDO969PvNqNYHIOW5v0m'
    # r = requests.get(BASE_URL + 'audio-features/'
    # + track_id, headers=headers)

    artist_albums = requests.get(BASE_URL + 'artists/' +
                                 beyonce_id + '/albums', headers=headers)
    # artist_data = artist.json()
    album_data = artist_albums.json()
    return album_data


# Unpack the JSON data into the form {field : array-like} to allow pandas
# and SQL to work effectively.
def make_dictionary_from_JSON(json_object, key_name: str) -> dict:
    new_dict = {key_name: []}

    if not json_object:
        return new_dict

    for i in range(len(json_object['items'])):
        new_dict["Albums"].append(json_object['items'][i]['name'])
    return new_dict


if __name__ == '__main__':
    response_data = issue_HTTP_request()
    albums_dict = make_dictionary_from_JSON(response_data, "Albums")

    # Create an engine object to make a path for a database.
    engine = db.create_engine('sqlite:///artist_info.db')
    # Create a data frame from the unpacked JSON data dictionary.
    df = pd.DataFrame.from_dict(albums_dict)

    # Convert the data frame to SQL.
    df.to_sql('artist', con=engine, if_exists='replace', index=False,
              dtype={"A": TEXT()})

    # Print out all the album releases made by the artist.
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM artist;")
                                          ).fetchall()
        print(pd.DataFrame(query_result))
