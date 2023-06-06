# spotify-auto-discovery
Small python application used for automaticaly records weekly discoveries using spotipy.

## Before starting
Install the dependencies <br>
`pip install -r requirements.txt`

Create .env file with the following environment Spotify developer infomation

    SPOTIPY_CLIENT_ID=""
    SPOTIPY_CLIENT_SECRET=""
    SPOTIPY_REDIRECT_URI=""

Also add the desired user name and ID

    SPOTIFY_USER=""<br>
    DISCOVER_WEEKLY_ID=""<br>

When firstly used it will prompt to ask for the auth token. 
Ppaste the opened URL (**to be improved adding the token in the env variables**)

    `Enter the URL you were redirected to: `