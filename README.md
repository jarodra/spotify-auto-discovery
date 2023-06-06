# spotify-auto-discovery
Small python application used for automaticaly records weekly discoveries using spotipy.

## Before starting
Install the dependencies

    pip install -r requirements.txt

Create .env file with the following environment Spotify developer infomation

    SPOTIPY_CLIENT_ID=""
    SPOTIPY_CLIENT_SECRET=""
    SPOTIPY_REDIRECT_URI=""

Also add the desired user name and ID

    SPOTIFY_USER=""
    DISCOVER_WEEKLY_ID=""

## Uses
Call the program and will autostart the token auth.
It will possibly fails due token expiration. In this case will be prompted.

    python main.py