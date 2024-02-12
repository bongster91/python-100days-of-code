from bs4 import BeautifulSoup
import requests
import spotipy
import json

URL = 'https://www.billboard.com/charts/hot-100/2000-08-12/'
CLIENT_ID = 'cf8f93e724004c7eabd5c554e00096b5'
CLIENT_SECRET = '33117e9ecd4f46bfaf73b4703694603c'
USERNAME = 'Bongster91'
REDIRECT_URI = 'https://example.com/'
SCOPE = 'playlist-modify-private'
SPOTIFY_BASE_URL = 'https://api.spotify.com'
SPOTIFY_URL = f"{SPOTIFY_BASE_URL}/users/{USERNAME}/playlists"

user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

billboard_response = requests.get(URL)
webpage = billboard_response.text
soup = BeautifulSoup(webpage, 'html.parser')
songs_list = soup.select('li ul li h3')
songs_list = [song.getText().strip() for song in songs_list]

oauth = spotipy.SpotifyOAuth(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET, 
    redirect_uri=REDIRECT_URI, 
    scope=SCOPE
)
sp = spotipy.Spotify(auth_manager=oauth)

user_id = sp.current_user()['id']

search_params = {
    "q": '2000-08-12%2520Imagine%2520That',
    'type': ['artist', 'track']
}
track_uris = []

for song in songs_list:
    track_search_response = sp.search(q=f"track:{song} year:2000-08-12", type=['track'])
    try:
        uri = track_search_response['tracks']['items'][0]['uri']
        track_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist.")
        
new_playlist = sp.user_playlist_create(user=user_id, name=f"new playlist", public=False)
new_playlist_id = new_playlist['id']

add_to_playlist = sp.playlist_add_items(playlist_id=new_playlist_id, items=track_uris, position=0)
