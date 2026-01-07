from django.urls import path
from .views import *

urlpatterns = [
    path('registraion', render_registration, name='registraion'),
    path('login', render_login, name='login'),
    path('welcome', render_welcome, name='welcome'),
    path('personal-account', render_personal_account, name='personal-account')
]