from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


travel_date = input("Which year do you want to travel to? Type the date iin this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


response = requests.get(f'https://www.billboard.com/charts/hot-100/{travel_date}/', headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
titles = [title.getText().strip() for title in soup.select('li ul li h3')]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
        username="Jason Zheng",
        client_id="Your Own",
        client_secret="Your Own"))

user_id = sp.current_user()['id']
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = travel_date.split('-')[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{travel_date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
