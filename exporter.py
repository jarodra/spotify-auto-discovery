import os
import time
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Write to GitHub Action summary and print output message
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
    global sp
    try: 
        scope = "playlist-modify-public"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=False))
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
        items = sp.playlist_items(playlist_id)["items"]
        tracks = [f"{item["track"]["artists"][0]["name"]} - {item["track"]["name"]}" for item in items]
        message = "Spotify weekly read"
        write_to_summary(f"**Step success:** {message}")
    except:
        message = "Error when reading the playlist"
        write_to_summary(f"**Step failed:** {message}")
        raise

if __name__ == "__main__":
    try:
        load_dotenv()
        USER_ID = os.getenv("SPOTIFY_USER")
        playlist_id = os.getenv("playlist_id")
        authenticate_spotify()
        read_playlist()
        with open(f"{playlist_id}.txt", 'w') as f:
            for track in tracks:
                print(track, file=f)
    except Exception as error:
        write_to_summary(f"## Workflow failed")
        print("An error occurred:", type(error).__name__, "–", error)
        exit(1) 
