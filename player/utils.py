# utils.py
from mutagen.mp3 import MP3

def get_mp3_metadata(file_path):
    try:
        audio = MP3(file_path)
        title = audio.get('TIT2', [None])[0]
        artist = audio.get('TPE1', [None])[0]
        album = audio.get('TALB', [None])[0]
        duration = audio.info.length  # Duration of the song in seconds
        return {
            'title': title,
            'artist': artist,
            'album': album,
            'duration': duration
        }
    except Exception as e:
        print(f"Error reading metadata: {e}")
        return None
