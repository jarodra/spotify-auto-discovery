import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import time

# Read environment variables
load_dotenv()
USER_ID = os.getenv("SPOTIFY_USER")
DISCOVER_WEEKLY_ID = os.getenv("DISCOVER_WEEKLY_ID")

# Authorization
scope = "playlist-modify-public"
try: 
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
except:
    print("Error during OAuth authorization")

# Read user playlist
try:
    items = spotify.playlist_items(DISCOVER_WEEKLY_ID)["items"]
    tracks = [item["track"]["external_urls"]["spotify"] for item in items]
    print("Spotify weekly read")
except:
    print("Error when reading the playlist")

# Create empty playlist
new_playlist_name = time.strftime("discover-weekly-%Y-KW%U")
try:
    new_playlist = spotify.user_playlist_create(USER_ID, new_playlist_name)
    print(f"New playlist created \"{new_playlist_name}\"")
except:
    print("Error when creating the playlist")

# Add tracks to the new playlist
try:
    spotify.playlist_add_items(new_playlist["id"], tracks, position=None)
    print("Songs added to the new playlist")
except:
    print("Error when adding the songs to the playlist")