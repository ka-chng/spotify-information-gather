import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'your_client_id'
client_secret = 'your_client_secret'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_user_info(user_url):
    user_id = user_url.split('/')[-1]
    user = sp.user(user_id)
    playlists = sp.user_playlists(user_id)

    highest_follower = max(user['followers']['items'], key=lambda x: x['followers']['total'])

    info = f"{user['display_name']} {user['external_urls']['spotify']} {user['followers']['total']}\n"
    info += f"{highest_follower['display_name']} {highest_follower['external_urls']['spotify']} {highest_follower['followers']['total']}\n"
    info += f"Total number of playlists: {len(playlists['items'])}"

    with open(f"{user['display_name']}.txt", 'w') as f:
        f.write(info)

user_input = input("Input user URL format: https://open.spotify.com/user/username")
get_user_info(f'{user_input}')
