from django.urls import path
from .views import render_playlist, render_playSongs

urlpatterns = [
    path('', render_playlist),
    path('play-song/<int:song_id>', render_playSongs, name='play_song')
]