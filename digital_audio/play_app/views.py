from django.shortcuts import render
from .models import Songs
from django.shortcuts import get_object_or_404

# Create your views here.
def render_playlist(request):
    list_songs = Songs.objects.all()
    return render(request, 'play_app/playlist.html', context={"list_songs": list_songs})

def render_playSongs(request, song_id):
    song = get_object_or_404(Songs, id=song_id)
    return render(request, 'play_app/play_songs.html', context={"song": song})