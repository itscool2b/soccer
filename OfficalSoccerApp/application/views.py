from django.shortcuts import render, redirect
from .forms import DashboardStatsForm, StatsPerGameForm, PlayerForm, PlayerGameStatsFormset
from .models import DashboardStats, StatsPerGame, Player
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# User login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
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
def dash(request):
    if request.method == 'POST':
        form = DashboardStatsForm(request.POST)
        if form.is_valid():
            dashboard_stat = form.save(commit=False)
            dashboard_stat.user = request.user
            dashboard_stat.save()
            messages.success(request, "Stats successfully saved.")
            return redirect('dash')
        else:
            messages.error(request, "Something went wrong. Please check the form and try again.")
    else:
        form = DashboardStatsForm()
    
    all_stats = DashboardStats.objects.filter(user=request.user)
    return render(request, "dash.html", {'form': form, 'all_stats': all_stats})

# View for creating or updating players
@login_required
def player_create_view(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.user = request.user
            player.save()
            messages.success(request, "Player created successfully.")
            return redirect('home')
    else:
        form = PlayerForm()
    return render(request, 'player_form.html', {'form': form})

# Home view showing games won and lost
@login_required
def home(request):
    games_lost = StatsPerGame.objects.filter(user=request.user, wl=False)
    games_won = StatsPerGame.objects.filter(user=request.user, wl=True)
    form = StatsPerGameForm()
    formset = PlayerGameStatsFormset()
    return render(request, 'index.html', {'form': form, 'formset': formset, 'games_lost': games_lost, 'games_won': games_won})

# View for adding a game and its stats
@login_required
def add_game(request):
    if request.method == 'POST':
        form = StatsPerGameForm(request.POST)
        formset = PlayerGameStatsFormset(request.POST)
        print(formset)
        if form.is_valid() and formset.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            formset.instance = game
            formset.save()
            messages.success(request, "Game and stats added successfully.")
    return redirect('home')


def playerhome(request):
    pass

def game(request):
    form = StatsPerGameForm()
    formset = PlayerGameStatsFormset()
    context = {
        'game_form': form,
        'player_stats_formset': formset
    }
    return render(request, 'addGame.html', context)