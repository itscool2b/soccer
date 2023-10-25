from django import forms
from .models import DashboardStats
from .models import StatsPerGame
from .models import Player
from .models import CustomUser
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
    class Meta:
        model = CustomUser
        fields = '__all__'