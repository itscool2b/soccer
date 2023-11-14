from django import forms
from .models import DashboardStats, StatsPerGame, Player
from django.contrib.auth.models import User
from .models import PlayerGameStats
from django.forms import inlineformset_factory
class DashboardStatsForm(forms.ModelForm):
    class Meta:
        model = DashboardStats
        exclude = ['user']

class StatsPerGameForm(forms.ModelForm):
    class Meta:
        model = StatsPerGame
        exclude = ['user']
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
        fields = ['player', 'goals', 'assists', 'completed_passes', 'total_passes', 'turnovers', 'saves', 'clean_sheets', 'red_cards', 'yellow_cards']
    
PlayerGameStatsFormset = inlineformset_factory(
    StatsPerGame, 
    PlayerGameStats, 
    fields=('player', 'goals', 'assists', 'completed_passes', 'total_passes', 
            'turnovers', 'saves', 'clean_sheets', 'yellow_cards', 'red_cards'), 
    extra=1, 
    can_delete=True
)