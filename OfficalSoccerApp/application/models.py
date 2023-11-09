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

class StatsPerGame(models.Model):
    vs = models.CharField(max_length=100, blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    completed_passes = models.IntegerField(blank=True, null=True)
    total_passes = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    saves = models.IntegerField(blank=True, null=True)
    clean_sheets = models.IntegerField(blank=True, null=True)
    red_card = models.ForeignKey('Player', on_delete=models.SET_NULL, related_name='red_cards', null=True, blank=True)
    yellow_card = models.ForeignKey('Player', on_delete=models.SET_NULL, related_name='yellow_cards', null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    wl = models.BooleanField(default=True, blank=True)
    assister = models.ForeignKey('Player', on_delete=models.SET_NULL, related_name='assisted_games', null=True, blank=True)
    goalscorer = models.ForeignKey('Player', on_delete=models.SET_NULL, related_name='scored_games', null=True, blank=True)
    cardgiven = models.ForeignKey('Player', on_delete=models.SET_NULL, related_name='card_given_games', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shutouts = models.ForeignKey('Player', on_delete=models.SET_NULL, related_name='shutouts_games', null=True, blank=True)
    savers = models.ForeignKey('Player', on_delete=models.SET_NULL, related_name='saves_games', null=True, blank=True)

class PlayerGameStats(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
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
    