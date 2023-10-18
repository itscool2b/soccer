from django import forms
from .models import DashboardStats
from .models import StatsPerGame
from .models import Player
from django.contrib.auth.models import User
class DashboardStatsForm(forms.ModelForm):
    class Meta:
        model = DashboardStats
        fields = '__all__'

class StatsPerGameForm(forms.ModelForm):
    class Meta:
        model = StatsPerGame
        fields = '__all__'

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']