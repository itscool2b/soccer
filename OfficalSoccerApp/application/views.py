from django.shortcuts import render
from .forms import DashboardStatsForm, StatsPerGameForm, PlayerForm, UserForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def usersignup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        username = form.cleaned_data['username']
        if form.is_valid():
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,"This username is already take")
            else:
                user = form.save()
                login(request, user)
        else:
            messages.error(request, "try again something went wrong")
        
    return

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return
        else:
            messages.error(request, "something went wrong")
    return

def userlogout(request):
    logout(request)
    return

@login_required
def DashBoardStats(request):
    if request.method == 'POST':
        info = DashboardStatsForm(request.POST)
        if info.is_valid():
            info.save()
            messages.success(request, "Data saved successfully")
        else:
            messages.error(request, "Invalid information. Please check the form.")
    return

@login_required
def StatsPerGame(request):
    if request.method == 'POST':
        info = StatsPerGameForm(request.POST)
        if info.is_valid():
            info.save()
            messages.success(request, "Data saved successfully")
        else:
            messages.error(request, "invalid info")
    return

    


