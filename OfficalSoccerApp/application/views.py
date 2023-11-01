from django.shortcuts import render, redirect
from .forms import UserForm, DashboardStatsForm, StatsPerGameForm
from .models import DashboardStats, StatsPerGame, Player
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404
from .models import PlayerGameStats
from .forms import PlayerGameStatsForm, PlayerGameStatsFormset
from django import forms
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
def dash(request):
    if request.method == 'POST':
        dstats = DashboardStatsForm(request.POST)
        if dstats.is_valid():
            form = dstats.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, "done")
            return redirect('dash')
        else:
            messages.error(request, "something went wrong")
            form = DashboardStatsForm
    all = DashboardStats.objects.all()
    return render(request, "dash.html",{
        'form': form,
        'all': all,
        

    })

@login_required
def statspergame(request):
    PlayerGameStatsFormset = forms.inlineformset_factory(StatsPerGame, PlayerGameStats, form=PlayerGameStatsForm, fields=('player', 'goals', 'assists', 'completed_passes', 'total_passes', 'turnovers', 'saves', 'clean_sheets', 'issued_card'), extra=5)
    
    if request.method == 'POST':
        form = StatsPerGameForm(request.POST)
        formset = PlayerGameStatsFormset(request.POST, prefix='playergamestats')
        
        player_forms = []
        for player in Player.objects.all():
            player_form = PlayerGameStatsForm(request.POST, prefix=f'player_{player.id}', instance=PlayerGameStats.objects.get_or_create(player=player)[0])
            player_forms.append((player, player_form))
            
            if player_form.is_valid():
                player_form.save()
        
        if form.is_valid() and formset.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            formset.instance = game
            formset.save()
            messages.success(request, "Data saved successfully")
            return redirect('stats')
    else:
        form = StatsPerGameForm()
        formset = PlayerGameStatsFormset(prefix='playergamestats')
        
        player_forms = []
        for player in Player.objects.all():
            player_form = PlayerGameStatsForm(prefix=f'player_{player.id}', instance=PlayerGameStats.objects.get_or_create(player=player)[0])
            player_forms.append((player, player_form))
    
    games_won = StatsPerGame.objects.filter(wl=True, user=request.user)
    games_lost = StatsPerGame.objects.filter(wl=False, user=request.user)
    
    return render(request, 'index.html', {
        'games_won': games_won,
        'games_lost': games_lost,
        'players': Player.objects.all(),
        'form': form,
        'playergamestats_formset': formset,
        'player_forms': player_forms,
    })
