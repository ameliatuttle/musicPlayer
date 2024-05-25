from django.urls import path
from . import views

# This maps out which view funcition should be called for a given URL pattern
urlpatterns = [
    path('', views.my_view, name='index'),
    path('song-info/', views.song_info, name='song_info'),
]