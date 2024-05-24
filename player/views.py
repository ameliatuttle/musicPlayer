from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
import random
from .utils import get_mp3_metadata

def my_view(request):
    music_dir = os.path.join(settings.BASE_DIR, 'static/music')
    mp3_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
    
    if not mp3_files:
        return HttpResponse("No MP3 files found in the directory", status=404)
    
    selected_file = random.choice(mp3_files)
    file_path = os.path.join(music_dir, selected_file)
    
    metadata = get_mp3_metadata(file_path)
    
    context = {
        'title': metadata.get('title', 'Unknown Title'),
        'artist': metadata.get('artist', 'Unknown Artist'),
        'album': metadata.get('album', 'Unknown Album'),
        'duration': metadata.get('duration', 'Unknown Duration'),
        'file_name': selected_file,
    }
    
    return render(request, 'index.html', context)

def song_info(request):
    file_name = request.GET.get('file_name')
    if not file_name:
        return HttpResponse("File name not provided", status=400)
    
    music_dir = os.path.join(settings.BASE_DIR, 'static/music')
    file_path = os.path.join(music_dir, file_name)
    
    if not os.path.exists(file_path):
        return HttpResponse("File not found", status=404)
    
    metadata = get_mp3_metadata(file_path)
    
    context = {
        'title': metadata.get('title', 'Unknown Title'),
        'artist': metadata.get('artist', 'Unknown Artist'),
        'album': metadata.get('album', 'Unknown Album'),
        'release_year': metadata.get('release_year', 'Unknown Year'),
        'genre': metadata.get('genre', 'Unknown Genre')
    }
    
    return render(request, 'song-info.html', context)
