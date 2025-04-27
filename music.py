'''import os
import assistant_details as ad
import pyautogui


def play_music():                                      #windows media player se hone keliye
    if ad.is_windows():
        music_path = r'G:\F drive\G drive\songs\01. Days Gone.mp3'
        os.startfile(music_path)
        return "Playing music"
    else:
        return "Can't play right now"

def play_pause_music():
    pyautogui.press('playpause')  # Play/Pause the music
    return "Toggled play/pause"

def next_song():
    pyautogui.press('nexttrack')  # Go to next song
    return "Playing next song"

def previous_song():
    pyautogui.press('prevtrack')  # Go to previous song
    return "Playing previous song"

def stop_music():
    pyautogui.press('stop')  # Stop the music
    return "Music stopped"'''




'''def pause_music():

    if ad.is_windows():
       
        return "Pause functionality not implemented yet."
    else:
        return "Can't pause right now"

def stop_music():

    if ad.is_windows():
        
        return "Stop functionality not implemented yet."
    else:
        return "Can't stop right now"

def next_song():

    if ad.is_windows():
        
        return "Next song functionality not implemented yet."
    else:
        return "Can't play next song right now"

def previous_song():  

    if ad.is_windows():
                                                                # No direct simple way to play previous song from CMD
        return "Previous song functionality not implemented yet."
    else:
        return "Can't play previous song right now"'''

'''import os
import pyautogui
import subprocess
import time

player = None

def play_music(song_path=r'G:\F drive\G drive\songs\01. Days Gone.mp3'):
    """Plays the given song with VLC (opens VLC window)."""
    
    # Correct VLC executable path
    vlc_path = r"D:\Accessories Softwares\VLC\vlc.exe"  # Update this path with your VLC path
    
    # Start VLC with the song path and force GUI window to open
    subprocess.Popen([vlc_path, song_path])
    
    # Wait for the song to start playing (increase sleep time if necessary)
    time.sleep(2)  # You can increase this time if VLC takes longer to load
    
    return "Playing music and opening VLC"

def play_pause_music():
    """Toggle play/pause using pyautogui."""
    pyautogui.press('playpause')
    return "Toggled play/pause"

def stop_music():
    """Stops music in VLC."""
    # Stop VLC by sending the stop command via pyautogui (simulates user pressing stop)
    pyautogui.press('stop')
    return "Music stopped"

def next_song():
    """Play the next song."""
    pyautogui.press('nexttrack')
    return "Playing next song"

def previous_song():
    """Play the previous song."""
    pyautogui.press('prevtrack')
    return "Playing previous song"'''    #this caused interruption of vlc and other media playing apps and even chrome/brave

'''import vlc
import time
import os

# Create a global player
player = None
# Optional: Play a random song from folder
def play_music(song_path=None):
    global player

    # Default folder
    folder_path = r'G:\F drive\G drive\songs'

    if song_path is None:
        # Pick the first song automatically
        songs = [file for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav', '.flac', '.mp4'))]
        if not songs:
            return "No songs found in the folder."
        song_path = os.path.join(folder_path, songs[0])

    if player:
        player.stop()  # Stop existing song first
    player = vlc.MediaPlayer(song_path)
    player.play()
    time.sleep(1)  # Give VLC time to start
    return f"Playing {os.path.basename(song_path)}"

def pause_music():
    global player
    if player:
        player.pause()
        return "Paused music."
    return "No music is playing."

def stop_music():
    global player
    if player:
        player.stop()
        return "Stopped music."
    return "No music is playing."

# For now, next/previous are dummy
def next_song():
    return " Next song functionality is coming soon."

def previous_song():
    return " Previous song functionality is coming soon."''' #just signle song ko play stop karne keliye (working)


import vlc
import time
import os
import random

# Global variables
player = None
playlist = []
current_index = 0

# Load all songs into playlist
def load_playlist(folder_path=r'G:\F drive\G drive\songs'):
    global playlist
    playlist = [os.path.join(folder_path, file) for file in os.listdir(folder_path)
                if file.endswith(('.mp3', '.wav', '.flac'))]
    playlist.sort()  # optional: sort alphabetically
    return playlist

def play_music(song_path=None):
    global player, current_index

    if not playlist:
        load_playlist()

    if song_path:
        if player:
            player.stop()
        player = vlc.MediaPlayer(song_path)
    else:
        if player:
            player.stop()
        player = vlc.MediaPlayer(playlist[current_index])

    player.play()
    time.sleep(1)
    return f"Playing {os.path.basename(playlist[current_index])}"

def pause_music():
    global player
    if player:
        player.pause()
        return "Paused music."
    return "No music is playing."

def stop_music():
    global player
    if player:
        player.stop()
        return "Stopped music."
    return "No music is playing."

def next_song():
    global current_index
    if not playlist:
        load_playlist()
    current_index = (current_index + 1) % len(playlist)  # loop to start
    return play_music()

def previous_song():
    global current_index
    if not playlist:
        load_playlist()
    current_index = (current_index - 1) % len(playlist)  # loop to end
    return play_music()

def shuffle_playlist():
    global playlist, current_index
    random.shuffle(playlist)
    current_index = 0
    return "Playlist shuffled!"















