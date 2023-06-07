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

## First uses
On the first time call the program and it will prompt a URI. 
Copy, paste it, and paste it back to your terminal. It will create a .cache file with the access token, and it will refresh authomaticaly. 
The following steps should be done after the .cache file has been created.

# Following uses
For single uses:

    python main.py

For image deployment there's a Dockerfile with an alpine distribution.
This Dockerfile has a cron job authomatized to run the python script once every Monday at 8:00.

    docker build --tag spotify-auto-discovery .
    docker run spotify-auto-discovery