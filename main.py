import subprocess
import time
import os
import pyautogui
from pynput import keyboard
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def startup():
    #set ver to w for automatic relaunches, g for keybind relaunches
    ver = "w"
    subprocess.Popen(['open', '-a', "/Applications/Spotify.app"])
    time.sleep(3)
    pyautogui.press('space')
    time.sleep(.5)
    pyautogui.hotkey('command', 'h')
    time.sleep(.25)
    pyautogui.hotkey('command', 'h')
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
                                                   client_secret="YOUR_APP_CLIENT_SECRET",
                                                   redirect_uri="YOUR_APP_REDIRECT_URI",
                                                   scope="user-read-currently-playing"))

def on_press(key):
    if key == keyboard.Key.caps_lock:
        subprocess.Popen(['open', '-a', "/Applications/Spotify.app"])
        time.sleep(.5)
        pyautogui.press('space')
        pyautogui.hotkey('command', 'h')
          
def wRestart():
    subprocess.call(['osascript', '-e', 'tell application "Spotify" to quit'])
    time.sleep(2)
    subprocess.Popen(['open', '-a', "/Applications/Spotify.app"])
    time.sleep(2)
    pyautogui.press('space')
    time.sleep(.5)
    pyautogui.hotkey('command', 'h')

def gRestart():
    subprocess.call(['osascript', '-e', 'tell application "Spotify" to quit'])
    time.sleep(2)
    subprocess.Popen(['open', '-a', "/Applications/Spotify.app", '-gj'])


startup()
if ver  == 'w':
    while True:
        try:
            if sp.current_user_playing_track()['currently_playing_type'] == 'ad':
                wRestart()
            time.sleep(3)
        except:
            pass
else:
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while True:
        try:
            if sp.current_user_playing_track()['currently_playing_type'] == 'ad':
                gRestart()
            time.sleep(3)
        except:
            pass
