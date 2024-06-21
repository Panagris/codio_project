# README
## Environment Variables
Environment variables must be set each time when developing in a remote
IDE such as CODIO. The environment variables may be set by following the below
command line commands:
```python
sudo nano ~/.bashrc  # To open the list of environment with nano.

# INSIDE NANO
  export SPOTIFY_CLIENT_ID= ''
  export SPOTIFY_CLIENT_SECRET=''
  export SPOTIPY_REDIRECT_URI=''
# SAVE AND EXIT NANO

source ~/.bashrc # To load the environment variables into the workspace.
```

## Spotify API
Follow [this link](https://developer.spotify.com/) to familiarize yourself with the Spotify API and create an account
to receive needed API client details.
