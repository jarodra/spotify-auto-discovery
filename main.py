import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import time

# Function to write to GitHub Action summary
def write_to_summary(message) :
    """Adds a job summary.

    Keyword arguments:
    message - Message to be printed
    """
    summary_file = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a") as file:
            file.write(message + "\n")
    else:
        print("GITHUB_STEP_SUMMARY is not set. Printing instead.")
        print(message)
    
# Read environment variables
load_dotenv()
USER_ID = os.getenv("SPOTIFY_USER")
DISCOVER_WEEKLY_ID = os.getenv("DISCOVER_WEEKLY_ID")

write_to_summary(f"## Spotify weekly save")

# Authorization
try: 
    scope = "playlist-modify-public"
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=False))
except:
    message = "Error during OAuth authorization"
    write_to_summary(f"**Step failed:** {message}")
    os._exit(1)
    
# Read user playlist
try:
    items = spotify.playlist_items(DISCOVER_WEEKLY_ID)
    # items = spotify.playlist_items(DISCOVER_WEEKLY_ID)["items"]
    tracks = [item["track"]["external_urls"]["spotify"] for item in items]
    message = "Spotify weekly read"
except:
    message = "Error when reading the playlist"
    print(message)
    write_to_summary(f"**Step failed:** {message}")
    os._exit(1)
    
# Create empty playlist
try:
    new_playlist_name = time.strftime("discover-weekly-%Y-KW%U")
    new_playlist = spotify.user_playlist_create(USER_ID, new_playlist_name)
    message = f"New playlist created {new_playlist_name}"
    print(message)
    write_to_summary(f"**Step success:** {message}")
except:
    message = "Error when creating the playlist"
    print(message)
    write_to_summary(f"**Step failed:** {message}")
    os._exit(1)

# Add tracks to the new playlist
try:
    spotify.playlist_add_items(new_playlist["id"], tracks, position=None)
    print("Songs added to the new playlist")
except:
    message = "Error when adding the songs to the playlist"
    print(message)
    write_to_summary(f"**Step failed:** {message}")
    os._exit(1)
