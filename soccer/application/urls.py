from . import views
from django.urls import path
urls = [
    path('', views.starting_page, name='startingpage'),
    path('login', views.login, name='login'),
    path('signup', views.sign_up, name='signup'),
    
]