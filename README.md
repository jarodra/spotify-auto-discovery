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

    SPOTIFY_USER=""<br>
    DISCOVER_WEEKLY_ID=""<br>

## First use
When firstly used it will prompt to ask for the auth token. 
Might fail on first use due token synchronizations.
Paste the opened URL (**to be improved adding the token in the env variables**)

    Enter the URL you were redirected to: 

## Following uses
Call the program and will autostart. It will possibly fails due token expiration. In this case will be prompted.

    python main.py