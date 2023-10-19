from django.shortcuts import render
from .forms import DashboardStatsForm, StatsPerGameForm, PlayerForm, UserForm
from .models import CustomUser
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        username = form.cleaned_data['username']
        if form.is_valid():
            user = form.save()
            login(request, user)
        
        if CustomUser.objects.filter(username=username).exists():
            message.error(request,"This username is already take")
    else:
        form = UserForm
    
    return

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return
    return

def logout(request):
    logout(request)
    return



