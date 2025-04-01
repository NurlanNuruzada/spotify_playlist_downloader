import json
import os
import time
import subprocess

import pandas as pd

# Load JSON file
df = pd.read_json("song_list1.json")
tracks = df.to_dict(orient="records")

# Create a directory for downloaded tracks
os.makedirs("tracks", exist_ok=True)

# Function to download a track using spotdl
def download_track(track_url, track_name=None):
    if track_name:
        print(f"\n🎵 Downloading {track_name} from {track_url}...")
    else:
        print(f"\n🎵 Downloading from {track_url}...")

    try:
        subprocess.run([
            "spotdl", track_url, "--output", "tracks/{artist} - {title}.mp3"
        ], check=True)
        print(f"✅ Download successful!")

    except subprocess.CalledProcessError:
        print(f"❌ Error downloading track.")

# Function to download tracks from JSON list
def download_from_json():
    total_tracks = len(tracks)
    if total_tracks == 0:
        print("⚠️ No tracks found in song_list1.json")
        return

    for i, track in enumerate(tracks, start=1):
        download_track(track["trackUrl"], track["trackName"])
        remaining_tracks = total_tracks - i
        if remaining_tracks > 0:
            print(f"🔄 {remaining_tracks} tracks remaining...\n")
        time.sleep(1)

    print("\n🎉 All tracks downloaded successfully!")

# Function to handle user input for manual search/download
def manual_download():
    query = input("🔎 Enter the song name or Spotify link: ").strip()

    if not query:
        print("⚠️ Invalid input. Please enter a valid song name or link.")
        return

    download_track(query, query)

# Main menu function
def main():
    print("\n🎶 Welcome to the Music Downloader! 🎶")
    print("1️⃣ Download all tracks from JSON")
    print("2️⃣ Search and download a song manually")
    choice = input("\n👉 Choose an option (1 or 2): ").strip()

    if choice == "1":
        download_from_json()
    elif choice == "2":
        manual_download()
    else:
        print("⚠️ Invalid choice. Please restart and select 1 or 2.")

if __name__ == "__main__":
    main()
