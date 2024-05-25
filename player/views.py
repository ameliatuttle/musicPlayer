from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
import random
from .utils import get_mp3_metadata

def my_view(request):
    # This defines the directory where the mp3 files are stored
    music_dir = os.path.join(settings.BASE_DIR, 'static/music')
    
    # Makes a list for the files
    mp3_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
    
    # If no mp3 files are found, return a 404 response
    if not mp3_files:
        return HttpResponse("No MP3 files found in the directory", status=404)
    
    # Randomly choose one of the MP3 files
    selected_file = random.choice(mp3_files)
    file_path = os.path.join(music_dir, selected_file)
    
    # Get the metadata of the selected MP3 file from get_mp3_metadata fucntion in utils
    metadata = get_mp3_metadata(file_path)
    
    # Create a context dictionary with the metadata and the file name
    context = {
        'title': metadata.get('title', 'Unknown Title'),
        'artist': metadata.get('artist', 'Unknown Artist'),
        'album': metadata.get('album', 'Unknown Album'),
        'duration': metadata.get('duration', 'Unknown Duration'),
        'file_name': selected_file,
    }
    
    # Render the 'index.html' template with the context data
    return render(request, 'index.html', context)

def song_info(request):
    # GThis gets the 'file_name' parameter from the URL query string
    file_name = request.GET.get('file_name')
    
    # If 'file_name' is not provided, return a 400 response
    if not file_name:
        return HttpResponse("File name not provided", status=400)
    
    # Define the full path of the mp3 file
    music_dir = os.path.join(settings.BASE_DIR, 'static/music')
    file_path = os.path.join(music_dir, file_name)
    
    # If the file does not exist, return a 404 response
    if not os.path.exists(file_path):
        return HttpResponse("File not found", status=404)
    
    # Get the metadata of the mp3 file
    metadata = get_mp3_metadata(file_path)
    
    # Create a context dictionary with the metadata
    context = {
        'title': metadata.get('title', 'Unknown Title'),
        'artist': metadata.get('artist', 'Unknown Artist'),
        'album': metadata.get('album', 'Unknown Album'),
        'release_year': metadata.get('release_year', 'Unknown Year'),
        'genre': metadata.get('genre', 'Unknown Genre')
    }
    
    # Render the 'song-info.html' template with the context data
    return render(request, 'song-info.html', context)

