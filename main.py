import os
import time
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy_anon import SpotifyAnon

# Function to write to GitHub Action summary and print output message
def write_to_summary(message) :
    """Adds a job summary.
    Keyword arguments:
        message - Message to be printed
    """
    summary_file = os.getenv("GITHUB_STEP_SUMMARY")
    print(message)
    if summary_file:
        with open(summary_file, "a") as file:
            file.write(message + "\n")
    else:
        print("GITHUB_STEP_SUMMARY is not set. Printing instead.")
        print(message)
    
# Authorization
def authenticate_spotify():
    global sp, sp_anon
    try: 
        scope = "playlist-modify-public"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=False))
        sp_anon = spotipy.Spotify(auth_manager=SpotifyAnon())
        message = "Auth completed"
        write_to_summary(f"**Step success:** {message}")
    except:
        message = "Error during OAuth authorization"
        write_to_summary(f"**Step failed:** {message}")
        raise
        
# Read user playlist
def read_playlist():
    global tracks
    try:
        items = sp_anon.playlist_items(DISCOVER_WEEKLY_ID)["items"]
        tracks = [item["track"]["external_urls"]["spotify"] for item in items]
        message = "Spotify weekly read"
        write_to_summary(f"**Step success:** {message}")
    except:
        message = "Error when reading the playlist"
        write_to_summary(f"**Step failed:** {message}")
        raise
    
# Create empty playlist
def create_playlist():
    global new_playlist
    try:
        new_playlist_name = time.strftime("discover-weekly-%Y-KW%U")
        new_playlist = sp.user_playlist_create(USER_ID, new_playlist_name)
        message = f"New playlist created {new_playlist_name}"
        write_to_summary(f"**Step success:** {message}")
    except:
        message = "Error when creating the playlist"
        write_to_summary(f"**Step failed:** {message}")
        raise

# Add tracks to the new playlist
def add_tracks_to_playlist():
    try:
        sp.playlist_add_items(new_playlist["id"], tracks, position=None)
        message = "Songs added to the new playlist"
        write_to_summary(f"**Step success:** {message}")
    except:
        message = "Error when adding the songs to the playlist"
        write_to_summary(f"**Step failed:** {message}")
        raise

if __name__ == "__main__":
    try:
        # Read environment variables
        load_dotenv()
        USER_ID = os.getenv("SPOTIFY_USER")
        DISCOVER_WEEKLY_ID = os.getenv("DISCOVER_WEEKLY_ID")
        write_to_summary(f"## Spotify weekly save")
        authenticate_spotify()
        read_playlist()
        create_playlist()
        add_tracks_to_playlist()
    except:
        write_to_summary(f"## Workflow failed")
        exit(1) 
