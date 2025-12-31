from django.urls import path
from .views import render_registration, render_login, render_welcome

urlpatterns = [
    path('registraion', render_registration, name='registraion'),
    path('login', render_login, name='login'),
    path('welcome', render_welcome, name='welcome'),
]