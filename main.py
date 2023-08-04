import time
from pynput import keyboard
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from funcs import restart, on_press, setup
from creds import client_id, client_secret, redirect_uri

#set ver to w for automatic relaunches, g for keybind relaunches
ver = "w"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="user-read-currently-playing"))
setup(ver)

while True:
    try:
        if sp.current_user_playing_track()['currently_playing_type'] == 'ad':
            restart(ver)
        time.sleep(3)
    except:
        pass
