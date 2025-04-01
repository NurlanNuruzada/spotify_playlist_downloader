import json
import os
import time
import subprocess

import pandas as pd

df = pd.read_json("song_list1.json")

tracks = df.to_dict(orient="records")

os.makedirs("tracks", exist_ok=True)

def download_track(track, index, total_tracks):
    track_url = track["trackUrl"]
    
    print(f"\n[{index}/{total_tracks}] Downloading {track['trackName']} from {track_url}...")

    try:
        subprocess.run([
            "spotdl", track_url, "--output", "tracks/{artist} - {title}.mp3"
        ], check=True)

        print(f"✅ {track['trackName']} downloaded successfully!")

    except subprocess.CalledProcessError:
        print(f"❌ Error downloading {track['trackName']}.")

def main():
    total_tracks = len(tracks)
    if total_tracks == 0:
        print("⚠️ No tracks found in song_list1.json")
        return

    for i, track in enumerate(tracks, start=1):
        download_track(track, i, total_tracks)
        remaining_tracks = total_tracks - i
        if remaining_tracks > 0:
            print(f"🔄 {remaining_tracks} tracks remaining...\n")
        time.sleep(1)

    print("\n🎉 All tracks downloaded successfully!")

if __name__ == "__main__":
    main()
