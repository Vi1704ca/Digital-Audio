from django.urls import path
from .views import render_album

urlpatterns = [
    path('album', render_album, name='album'),
   # path('play-song/<int:song_id>', render_playSongs, name='play_song')
]