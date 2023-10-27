from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.usersignup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('dashboard/stats/', views.dashboard_stats_view, name='dashboard_stats'),
    path('stats/per/game/', views.stats_per_game_view, name='stats_per_game'),
    path('dashboard/stats/update/', views.dashboard_stats_update, name='dashboard_stats_update'),
    path('games/', views.all_games, name='all_games'),
    path('game/<int:id>/', views.game_detail, name='game_detail'),
    path('players/', views.all_players, name='all_players'),
    path('player/<int:id>/', views.player_detail, name='player_detail'),
]
