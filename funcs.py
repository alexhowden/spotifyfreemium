import subprocess
import time
import pyautogui
from pynput import keyboard

def setup():
    subprocess.Popen(['open', '-a', "/Applications/Spotify.app"])
    time.sleep(3)
    pyautogui.press('space')
    time.sleep(.5)
    pyautogui.hotkey('command', 'h')
    time.sleep(.25)
    pyautogui.hotkey('command', 'h')

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
