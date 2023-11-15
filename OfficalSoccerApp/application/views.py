from django.shortcuts import render, redirect, get_object_or_404
from .forms import DashboardStatsForm, StatsPerGameForm, PlayerForm, PlayerGameStatsFormset
from .models import DashboardStats, StatsPerGame, Player
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
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
    stats = get_object_or_404(DashboardStats, user=request.user)
    stats.update_game_stats()
    stats.update_totals()
    try:
        dash = DashboardStats.objects.get(user=request.user)
    except DashboardStats.DoesNotExist:
        # Handle the case where DashboardStats does not exist for the user
        dash = None
    return render(request,'dash.html', {'stats': dash})
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
    return redirect('playerhome')

# Home view showing games won and lost
@login_required
def home(request):
    games_lost = StatsPerGame.objects.filter(user=request.user, wl=False)
    games_won = StatsPerGame.objects.filter(user=request.user, wl=True)
    
    return render(request, 'index.html', {'games_lost': games_lost, 'games_won': games_won})

# View for adding a game and its stats
@login_required
def add_game(request):
    if request.method == 'POST':
        game_form = StatsPerGameForm(request.POST)
        if game_form.is_valid():
            with transaction.atomic():
                new_game = game_form.save(commit=False)
                new_game.user = request.user
                new_game.save()

                for player in Player.objects.all():
                    formset = PlayerGameStatsFormset(request.POST, prefix=str(player.id))
                    if formset.is_valid():
                        instances = formset.save(commit=False)
                        for instance in instances:
                            instance.game = new_game
                            instance.player = player
                            instance.save()

                messages.success(request, "New game and player stats added successfully.")
                return redirect('home')
        else:
            messages.error(request, "There were errors in the submission.")
    else:
        game_form = StatsPerGameForm()

    # Create an empty formset for each player
    player_stats_formsets = {
        player.id: PlayerGameStatsFormset(prefix=str(player.id))
        for player in Player.objects.all()
    }

    return render(request, 'addGame.html', {
        'game_form': game_form,
        'player_stats_formsets': player_stats_formsets,
    })



def playerhome(request):
    players = Player.objects.all()
    form = PlayerForm()
    context = {
        'players': players,
        'form': form
    }
    return render(request, 'player.html', context)


