from django.shortcuts import render, redirect
from .forms import UserForm, DashboardStatsForm, StatsPerGameForm
from .models import CustomUser, DashboardStats, StatsPerGame, Player

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# User registration view
@require_http_methods(["GET", "POST"])
def usersignup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('some_redirect_url')  # Replace with your desired redirect URL
        else:
            messages.error(request, "Try again, something went wrong")
    return render(request, 'signup.html', {'form': UserForm()})

# User login view
@require_http_methods(["GET", "POST"])
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('some_redirect_url')  # Replace with your desired redirect URL
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

# User logout view
@login_required
def userlogout(request):
    logout(request)
    return redirect('some_redirect_url')  # Replace with your desired redirect URL

# DashboardStats creation view
@login_required
@require_http_methods(["GET", "POST"])
def dashboard_stats_view(request):
    if request.method == 'POST':
        info = DashboardStatsForm(request.POST)
        if info.is_valid():
            temp = info.save(commit=False)
            temp.user = request.user
            temp.save()
            messages.success(request, "Data saved successfully")
        else:
            messages.error(request, "Invalid information. Please check the form")
    return render(request, 'dashboard_stats.html', {'form': DashboardStatsForm()})

# StatsPerGame creation view
@login_required
@require_http_methods(["GET", "POST"])
def stats_per_game_view(request):
    if request.method == 'POST':
        info = StatsPerGameForm(request.POST)
        if info.is_valid():
            stats_per_game = info.save(commit=False)
            stats_per_game.user = request.user
            stats_per_game.save()
            messages.success(request, "Data saved successfully")
        else:
            messages.error(request, "Invalid information. Please check the form")
    return render(request, 'stats_per_game.html', {'form': StatsPerGameForm()})

# DashboardStats update view
@login_required
@require_http_methods(["GET", "POST"])
def dashboard_stats_update(request):
    instance, created = DashboardStats.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = DashboardStatsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully")
        else:
            messages.error(request, "Error")
    return render(request, 'dashboard_stats_update.html', {'form': DashboardStatsForm(instance=instance)})

# AllGames view
def all_games(request):
    games = StatsPerGame.objects.all()
    return render(request, 'index.html', {'games': games})

# GameDetail view
def game_detail(request, id):
    game = StatsPerGame.objects.get(pk=id)
    return render(request, 'game_detail_template.html', {'game': game})

# AllPlayers view
def all_players(request):
    all_players = Player.objects.all()
    return render(request, 'player_list_template.html', {'players': all_players})

# PlayerDetail view
def player_detail(request, id):
    player = Player.objects.get(pk=id)
    return render(request, 'player_detail_template.html', {'player': player})
