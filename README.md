# spotify-auto-discovery
Personal project to learn spotify api through python's spotipy library, authentications and different deployment applications. 

Currently is usable and several platforms are possible to be used
- [x] Manual
- [x] Docker
- [x] Docker-compose
- [X] Kubernetes Cronjob

### Clone the repository
Clone the repository which the following command

    git clone https://github.com/Durgrim/spotify-auto-discovery.git

### Before starting
Install the dependencies.  
Use virtual environments as this will be deployed on docker.  
If you can to use the script in your local machine, just install the requirements.  

    python3 -m venv env
    source env/bin/activate
    cd app
    python3 -m pip install -r requirements.txt

Create an .env file with the following [Spotify developer](https://developer.spotify.com/) infomation.
[Use the recommended (http://localhost:8080) to automatic refresh of authentication token](https://github.com/spotipy-dev/spotipy/blob/587baec9b95da6c45e45f0f8e5b2577bda780980/spotipy/oauth2.py#L374..L383)

    SPOTIPY_CLIENT_ID="your_spotify_developer_id"
    SPOTIPY_CLIENT_SECRET="your_spotify_developer_secret"
    SPOTIPY_REDIRECT_URI="your_spotify_developer_redurect_uri"
    SPOTIFY_USER="your_spotify_user_name"
    DISCOVER_WEEKLY_ID="discover_playlist_id"

### First uses
Execute in your local machine the following commands:

    cd app
    python3 main.py

On this first time call the program and it will prompt a URI.  
This authorization is required as we're using Authorization Code flow on Spotipy through SpotifyOAuth.
Copy, paste it, and paste it back to your terminal.  
It will create a .cache file with the access token, and it will refresh authomaticaly.  
The following steps should be done after the .cache file has been created.  

### Following uses

#### Manual use
If you can to use the script manually in your local machine, just repeat the previous step.  

#### Docker/Docker-compose with cron deployment
For image deployment there's a Dockerfile with an alpine distribution implemented.  
This Dockerfile has a cron job authomatized to run the python script once every Monday at 8:00.

    docker build --tag spotify-auto-discovery .
    docker run -d spotify-auto-discovery

If you prefer to use Docker Compose just use `docker compose up -d` or `docker compose down`.  

#### Kubernetes cronjob deployment
If you prefer to user a kubernetes clusters:

    docker build -t spotify-auto-discovery-kubernetes -f Dockerfile-kubernetes .
    kubectl apply -f cronjob.yaml
