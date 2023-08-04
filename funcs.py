import subprocess
import time
import pyautogui
from pynput import keyboard
from spotifyadkiller import ver

def setup():
    subprocess.Popen(['open', '-a', "/Applications/Spotify.app"])
    time.sleep(3)
    pyautogui.press('space')
    time.sleep(.5)
    pyautogui.hotkey('command', 'h')
    time.sleep(.25)
    pyautogui.hotkey('command', 'h')
    if ver == 'g':
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

def on_press(key):
    if key == keyboard.Key.caps_lock:
        subprocess.Popen(['open', '-a', "/Applications/Spotify.app"])
        time.sleep(.5)
        pyautogui.press('space')
        pyautogui.hotkey('command', 'h')
          
def restart():
    if ver == 'w':
        subprocess.call(['osascript', '-e', 'tell application "Spotify" to quit'])
        time.sleep(2)
        subprocess.Popen(['open', '-a', "/Applications/Spotify.app"])
        time.sleep(2)
        pyautogui.press('space')
        time.sleep(.5)
        pyautogui.hotkey('command', 'h')
    else:
        subprocess.call(['osascript', '-e', 'tell application "Spotify" to quit'])
        time.sleep(2)
        subprocess.Popen(['open', '-a', "/Applications/Spotify.app", '-gj'])
