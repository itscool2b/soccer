from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

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

    def __str__(self):
        return self.name

    def total_goals(self):
        return self.playergamestats_set.aggregate(Sum('goals'))['goals__sum'] or 0

    def total_assists(self):
        return self.playergamestats_set.aggregate(Sum('assists'))['assists__sum'] or 0

    def total_completed_passes(self):
        return self.playergamestats_set.aggregate(Sum('completed_passes'))['completed_passes__sum'] or 0

    def total_total_passes(self):
        return self.playergamestats_set.aggregate(Sum('total_passes'))['total_passes__sum'] or 0

    def total_turnovers(self):
        return self.playergamestats_set.aggregate(Sum('turnovers'))['turnovers__sum'] or 0

    def total_saves(self):
        return self.playergamestats_set.aggregate(Sum('saves'))['saves__sum'] or 0

    def total_clean_sheets(self):
        return self.playergamestats_set.aggregate(Sum('clean_sheets'))['clean_sheets__sum'] or 0

    def total_yellow_cards(self):
        return self.playergamestats_set.aggregate(Sum('yellow_cards'))['yellow_cards__sum'] or 0

    def total_red_cards(self):
        return self.playergamestats_set.aggregate(Sum('red_cards'))['red_cards__sum'] or 0

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