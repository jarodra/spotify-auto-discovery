# spotify-auto-discovery
Personal project to learn spotify api through python's spotipy library, authentications and different deployment applications. 

This branch allows the start up with GitHub Actions
- [x] Manual
- [x] GitHub actions 
- [x] Docker (containers branch)
- [x] Server (raspberry pi)

### Preparing up
Fork the repository and clone it to your local environment.

### Setting up the environment
Set up the Spotify Developer account and get the credentials.

Define the following variables (in a local file called .env):
```
    SPOTIPY_CLIENT_ID="your_spotify_developer_id"
    SPOTIPY_CLIENT_SECRET="your_spotify_developer_secret"
    SPOTIPY_REDIRECT_URI="your_spotify_developer_redurect_uri"
    SPOTIFY_USER="your_spotify_user_name"
    DISCOVER_WEEKLY_ID="discover_playlist_id"
```

### First use (Manual use)
Execute in your local machine the following commands:
    pip3 install -r requirements.txt
    python3 main.py

On this first time call the program and it will prompt a URI.  
This authorization is required as we're using Authorization Code flow on Spotipy through SpotifyOAuth.
Copy, paste it, and paste it back to your terminal.  
It will create a .cache file with the access token, and it will refresh authomaticaly.  
The following steps should be done after the .cache file has been created. 
In this .cache file there is the access_token (and expiration time expires_at) and refresh_token.

### Following uses
#### GitHub actions CI
An option to deploy the app in a Github runner machine and not depend on your own resourses is to use a Cloud Provider as Google, AWS or Azure.
Define in the forked repository the following secrets (from the .env or from the .cache files).

**.env (from Spotify Developer):**
- DISCOVER_WEEKLY_ID
- SPOTIFY_USER
- SPOTIPY_CLIENT_ID
- SPOTIPY_CLIENT_SECRET	
- SPOTIPY_REDIRECT_URI

**.cache (created on first manual execution):**
- ACCESS_TOKEN
- REFRESH_TOKEN
- EXPIRES_AT

#### Server
If you already have a virtual machine or a local machine that is going to be running at the desired schedule and want to use it for this purpose you can!
Just leave .cache and .env in your and use `crontab -e` add a new line like the following one, save and exit:

    0 8 * * 1 /usr/bin/python3 /path/to/my_script/main.py
