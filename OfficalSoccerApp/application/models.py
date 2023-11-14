from django.db import models
from django.contrib.auth.models import User


class DashboardStats(models.Model):
    games_played = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    total_goals = models.IntegerField()
    total_saves = models.IntegerField()
    total_assists = models.IntegerField()
    total_clean_sheets = models.IntegerField()
    total_yellow_cards = models.IntegerField()
    total_red_cards = models.IntegerField()
    total_blue_cards = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Player(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # You might want to add fields for total goals, assists, etc.

class StatsPerGame(models.Model):
    vs = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    wl = models.BooleanField(default=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Removed fields for goals, assists, etc. as they will be in PlayerGameStats

class PlayerGameStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(StatsPerGame, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    completed_passes = models.IntegerField(default=0)
    total_passes = models.IntegerField(default=0)
    turnovers = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)