import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.billboard.com/charts/hot-100/"

# date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")
# header = {Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36}

def get_song(song, date):
    #sp.search(song, date)
    return {
        "track": song,
        "url": f"spotify:track:MOCK_{song.replace(' ', '_')}",
        
    }

def create_playlist(urls, name):
    playlist = []
    print(f"Playlist {name} created with 100 Songs")
    for song in urls:
        playlist.append((song["track"], song["url"]))
    return playlist

now = datetime.now()
response = requests.get(URL)
response.raise_for_status()
web_page = (response.text)

soup = BeautifulSoup(web_page, "html.parser")
all_songs = soup.find_all(class_="o-chart-results-list-row-container")



song_names = [song.select_one("h3").getText().strip() for song in all_songs]
print(song_names)
print(len(song_names))

track_urls = []

for song in song_names:
    try:
        result = get_song(song, now)
        track_urls.append(result)
    except ValueError:
        print(f"{song} not found, skipping")

playlist = create_playlist(track_urls, "Top 100")
print(playlist)