from django.shortcuts import render
from .utils import get_mp3_metadata

import os
import random
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .utils import get_mp3_metadata

def my_view(request):
    music_dir = os.path.join(settings.BASE_DIR, 'static/music')
    mp3_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
    
    if not mp3_files:
        return HttpResponse("No MP3 files found in the directory", status=404)
    
    selected_file = random.choice(mp3_files)
    file_path = os.path.join(music_dir, selected_file)
    
    # Determine the index of the selected file in the list
    selected_index = mp3_files.index(selected_file)
    
    # Determine the index of the next file in the playlist
    next_index = (selected_index + 1) % len(mp3_files)
    
    next_file = mp3_files[next_index]
    next_file_path = os.path.join(music_dir, next_file)
    
    metadata = get_mp3_metadata(file_path)
    next_metadata = get_mp3_metadata(next_file_path)
    
    context = {
        'title': metadata.get('title', 'Unknown Title'),
        'artist': metadata.get('artist', 'Unknown Artist'),
        'album': metadata.get('album', 'Unknown Album'),
        'duration': metadata.get('duration', 'Unknown Duration'),
        'next_title': next_metadata.get('title', 'Unknown Title'),
        'next_artist': next_metadata.get('artist', 'Unknown Artist'),
        'next_album': next_metadata.get('album', 'Unknown Album'),
        'next_duration': next_metadata.get('duration', 'Unknown Duration'),
        'file_name': selected_file,
    }
    
    return render(request, 'index.html', context)
