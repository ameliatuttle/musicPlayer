# Use the mutagen library for audio info
from mutagen.mp3 import MP3

def get_mp3_metadata(file_path):
    try:
        # Load the mp3 file into a variable
        audio = MP3(file_path)
        
        # Get the metadata with default values in case the field is not present
        title = audio.get('TIT2', [None])[0]
        artist = audio.get('TPE1', [None])[0]
        album = audio.get('TALB', [None])[0]
        release_year = audio.get('TDRC', [None])[0]
        genre = audio.get('TCON', [None])[0]
        
        # Return a dictionary with the metadata
        return {
            'title': title,
            'artist': artist,
            'album': album,
            'release_year': release_year,
            'genre': genre,
        }
    except Exception as e:
        # Print an error message if there's an issue reading the metadata
        print(f"Error reading metadata: {e}")
        return None