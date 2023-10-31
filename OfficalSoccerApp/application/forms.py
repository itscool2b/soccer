from django import forms
from .models import DashboardStats, StatsPerGame, Player
from django.contrib.auth.models import User
from .models import PlayerGameStats
from django.forms import modelformset_factory
class DashboardStatsForm(forms.ModelForm):
    class Meta:
        model = DashboardStats
        exclude = ['user']

class StatsPerGameForm(forms.ModelForm):

    class Meta:
        model = StatsPerGame
        exclude = ['user', 'players']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password']


class PlayerGameStatsForm(forms.ModelForm):
    class Meta:
        model = PlayerGameStats
        fields = ['player', 'goals', 'assists', 'completed_passes', 'total_passes', 'turnovers', 'saves', 'clean_sheets', 'issued_card']
    
PlayerGameStatsFormset = modelformset_factory(PlayerGameStats, form=PlayerGameStatsForm, extra=1)