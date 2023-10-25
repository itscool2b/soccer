from django.urls import path
from . import views
urlpatterns = [

    path('signup/', views.usersignup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path("StatsPerGame/", views.StatsPerGame, name='StatsPerGame'),
    path("DashBoardStats/", views.DashBoardStats, name='DashboardStats')
]
