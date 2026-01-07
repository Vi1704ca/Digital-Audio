from django.shortcuts import render

# Create your views here.
def render_home_page(request):
    return render(request, 'core_app/home.html')