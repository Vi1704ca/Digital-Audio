from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.db.utils import IntegrityError

# Create your views here.
def render_registration(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordConfirm = request.POST.get('passwordConfirm')
        if password == passwordConfirm:
            try:
                User.objects.create_user(username=username, password=password, email=email)
                return redirect('login')
            except IntegrityError:
                error = "Такий користовач вже існує"
        else:
            error = "Паролі не співпадають"
    return render(request, 'user_app/registration.html', context={"error": error})


def render_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('welcome')
    return render(request, 'user_app/login.html')


def render_welcome(request):
    return render(request, 'user_app/welcome.html')