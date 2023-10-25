from django.urls import path
from . import views
urlpatterns = [

    path('signup/', views.usersignup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path("StatsPerGame/", views.StatsPerGame, name='StatsPerGame'),
    path("DashboardStats/", views.DashboardStats, name='DashboardStats'),
    path("games/<int:id>/", views.AllGames, name='all')
]
