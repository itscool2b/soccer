from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("dash/", views.all_games, name="dash"),
    path("save/", views.save_game, name="save")
]
