from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/", views.dash, name='dash'),
    path("home/", views.home, name='home'),
    path("add_game/", views.add_game, name='add_game'),
    path("player/", views.player_create_view, name="createplayer"),
    path("playerhome/", views.playerhome, name='playerhome')
]
