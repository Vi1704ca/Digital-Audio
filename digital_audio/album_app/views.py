from django.shortcuts import render

# Create your views here.
def render_album(request):
    return render(request, 'album_app/album.html')