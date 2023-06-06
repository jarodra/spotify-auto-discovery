# spotify-auto-discovery
Small python application used for automaticaly records weekly discoveries using spotipy.

## Before starting
Install the dependencies

    pip install -r requirements.txt

Create .env file with the following environment Spotify developer infomation.
[Recommended http://localhost:8080 or similar to automatic retrieval of authentication code](https://github.com/spotipy-dev/spotipy/blob/587baec9b95da6c45e45f0f8e5b2577bda780980/spotipy/oauth2.py#L374..L383)

    SPOTIPY_CLIENT_ID=""
    SPOTIPY_CLIENT_SECRET=""
    SPOTIPY_REDIRECT_URI="".

Also add the desired user name and ID

    SPOTIFY_USER=""
    DISCOVER_WEEKLY_ID=""

## Uses
Call the program and will autostart the token auth.
It will possibly fails due token expiration. In this case will be prompted.

    python main.py