from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("createplayer/", views.player_create_view, name="createplayer"),
    path("home/", views.home, name='home'),
    path("dash/", views.dash, name='dash'),
    path("playerstats/", views.playerhome, name="playerhome"),
    path("create/", views.playerform, name="playerform")
]
