# spotify-auto-discovery
Small python application used for automaticaly records weekly discoveries using spotipy.

## Before starting
Install the dependencies <br>
`pip install -r requirements.txt`

Create .env file with the following environment Spotify developer infomation<br>
        SPOTIPY_CLIENT_ID=""<br>
        SPOTIPY_CLIENT_SECRET=""<br>
        SPOTIPY_REDIRECT_URI=""<br>
Also add the desired user name and ID<br>
        SPOTIFY_USER=""<br>
        DISCOVER_WEEKLY_ID=""<br>

When firstly used it will prompt to ask for the auth token. You need to paste the URL that is opened (to be improved adding the token in the env variables)
`Enter the URL you were redirected to: `