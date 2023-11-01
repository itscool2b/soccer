from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("statspergame/", views.dash, name="stats"),
    path("dahs/", views.dash, name='dash')
]
