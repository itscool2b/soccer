from django.shortcuts import render, redirect
from .forms import UserForm, DashboardStatsForm, StatsPerGameForm
from .models import DashboardStats, StatsPerGame 
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404
from .models import PlayerGameStats, Player
from .forms import PlayerGameStatsForm, PlayerForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

def playerform(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            yes = form.save(commit=False)
            yes.user = request.user
            yes.save()
            messages.success(request, "YAY")
            return redirect('playerhome')
        else:
            form = PlayerForm()
            messages.error(request, "something went wrong")
            return redirect('playerhome')
        
def playerhome(request):
    players = Player.objects.prefetch_related('playerstats')
    return render(request, 'player.html', {
        'players': players
    })

def update_player_stats(user, form_data):
    """
    This function updates the stats of a player.
    """
    player_stats, _ = PlayerGameStats.objects.update_or_create(
        user=user,
        defaults=form_data
    )
    return player_stats

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
            print("Stats saved for user:", request.user.username)  # Printing to console
            return redirect('dash')
        else:
            print("Form errors:", form.errors)  # Print form errors if not valid
            messages.error(request, "Something went wrong. Please check the form and try again.")
    else:
        form = DashboardStatsForm()
    
    all_stats = DashboardStats.objects.all()
    print("All Stats:", all_stats)  # Print all_stats queryset to console

    return render(request, "dash.html", {
        'form': form,
        'all_stats': all_stats,
    })




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
    return redirect('home')

@login_required
def home(request):
    games_lost = StatsPerGame.objects.filter(wl=False)
    games_won = StatsPerGame.objects.filter(wl=True)

    return render(request, 'index.html', {
        "games_lost":games_lost,
        "games_won": games_won
    })

@login_required
def updateplayerstats(request):
    if request.method == 'POST':
        form = PlayerGameStatsForm(request.POST)
        if form.is_valid():
            
            update_player_stats(request.user, form.cleaned_data)
            messages.success(request, "Player stats updated successfully.")
            return redirect('home')  
        else:
            messages.error(request, "There was an error updating the player stats.")
    else:
        
        player_stats_instance = PlayerGameStats.objects.filter(user=request.user).first()
        form = PlayerGameStatsForm(instance=player_stats_instance)
    
    return redirect('home')


def statsform(request):
    if request.method == 'POST':
        form = StatsPerGameForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.user = request.user
            form2.save()
            messages.success(request, "amazing")
            return redirect('home')
        else:
            messages.error(request, "something went wrong")
            return redirect('home')
            