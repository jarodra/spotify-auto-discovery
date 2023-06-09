# spotify-auto-discovery
Small python application used for automaticaly records weekly discoveries using spotipy.


## Before starting
Install the dependencies.  
Use virtual environments as this will be deployed on docker.  
If you can to use the script in your local machine, just install the requirements.  

    python3 -m venv env
    source env/bin/activate
    cd app
    python3 -m pip install -r requirements.txt

Create an .env file with the following Spotify developer infomation.  
[Used the recommended (http://localhost:8080) to automatic refresh of authentication token](https://github.com/spotipy-dev/spotipy/blob/587baec9b95da6c45e45f0f8e5b2577bda780980/spotipy/oauth2.py#L374..L383)

    SPOTIPY_CLIENT_ID=""
    SPOTIPY_CLIENT_SECRET=""
    SPOTIPY_REDIRECT_URI="".

Also add the desired user name and ID

    SPOTIFY_USER=""
    DISCOVER_WEEKLY_ID=""

## First uses
Execute in your local machine the following commands:

    cd app
    python3 main.py

On this first time call the program and it will prompt a URI.  
This authorization is required as we're using Authorization Code flow on Spotipy through SpotifyOAuth.
Copy, paste it, and paste it back to your terminal.  
It will create a .cache file with the access token, and it will refresh authomaticaly.  
The following steps should be done after the .cache file has been created.  

# Following uses
If you can to use the script in your local machine, just repeat the previous step.  

For image deployment there's a Dockerfile with an alpine distribution implemented.  
This Dockerfile has a cron job authomatized to run the python script once every Monday at 8:00.

    docker build --tag spotify-auto-discovery .
    docker run -d spotify-auto-discovery

If you prefer to use Docker Compose just use `docker compose up -d` or `docker compose down`.  