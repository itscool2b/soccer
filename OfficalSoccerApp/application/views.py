from django.shortcuts import render, redirect
from .forms import UserForm, DashboardStatsForm, StatsPerGameForm
from .models import DashboardStats, StatsPerGame
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User




from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dash')
    else:
        form = AuthenticationForm(request)
    return render(request, 'login-signup.html', {'form': form})



# User logout view
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# DashboardStats creation view
@login_required
@require_http_methods(["GET", "POST"])
def dashboard_stats_view(request):
    if request.method == 'POST':
        form = DashboardStatsForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            messages.success(request, "Data saved successfully")
            return redirect('dash')
        else:
            messages.error(request, "Invalid information. Please check the form")
    else:
        form = DashboardStatsForm()
    return render(request, 'dashboard_stats.html', {'form': form})

# StatsPerGame creation view
@login_required
@require_http_methods(["GET", "POST"])
def stats_per_game_view(request):
    if request.method == 'POST':
        form = StatsPerGameForm(request.POST)
        if form.is_valid():
            stats_per_game = form.save(commit=False)
            stats_per_game.user = request.user
            stats_per_game.save()
            messages.success(request, "Data saved successfully")
            return redirect('dash')
        else:
            messages.error(request, "Invalid information. Please check the form")
    else:
        form = StatsPerGameForm()
    return render(request, 'stats_per_game.html', {'form': form})

# AllGames view
@login_required
def all_games(request):
    games_won = StatsPerGame.objects.filter(wl=True, user=request.user)
    games_lost = StatsPerGame.objects.filter(wl=False, user=request.user)
    print('Games Won:', games_won)  # Add this line
    print('Games Lost:', games_lost)
    return render(request, 'index.html', {'games_won': games_won, 'games_lost': games_lost})

@login_required
def save_game(request):
    if request.method == 'POST':
        form = StatsPerGameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            return redirect("dash")
        else:
            form = StatsPerGameForm()
        return render(request, 'index.html', {'form': form})