#!/usr/bin/env python3
# interdimensional-cable.py

import re
import requests
import webbrowser

def create_youtube_playlist_link(video_ids):
    # Combine the video IDs into a comma-separated string
    video_id_string = ','.join(video_ids)

    # Build the URL for the playlist
    playlist_url = f'https://www.youtube.com/watch_videos?video_ids={video_id_string}'

    return playlist_url

url = "https://www.reddit.com/r/interdimensionalCable/hot.json"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
json_data = response.json()

pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?([a-zA-Z0-9_-]{11})"

video_ids = []

for post in json_data["data"]["children"]:
    text = post["data"]["url_overridden_by_dest"]
    matches = re.findall(pattern, text)
    for match in matches:
        video_ids.append(match)

link = create_youtube_playlist_link(video_ids)
webbrowser.open(link)