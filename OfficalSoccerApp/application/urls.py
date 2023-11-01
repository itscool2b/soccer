from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("statspergame/", views.statspergame, name="stats"),
    #path("dash/", views.dash, name='dash')
]
