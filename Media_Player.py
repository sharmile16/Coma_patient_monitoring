import time
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc


def play_alarm():
    media = vlc.MediaPlayer('alarmbak.wav')
    media.play()

    timeout = time.time() + 3
    while True:
        if time.time() > timeout:
            media.stop()
            break