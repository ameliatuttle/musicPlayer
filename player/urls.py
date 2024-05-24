from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='index'),
    path('song-info/', views.song_info, name='song_info'),
]