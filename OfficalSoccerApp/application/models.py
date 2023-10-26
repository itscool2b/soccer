from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.IntegerField()

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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
class Player(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    assists = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    goals = models.IntegerField()
    shutouts = models.IntegerField()
    saves = models.IntegerField()
class StatsPerGame(models.Model):
    vs = models.CharField(max_length=100)
    goals = models.IntegerField()
    assists = models.IntegerField()
    completed_passes = models.IntegerField()
    total_passes = models.IntegerField()
    turnovers = models.IntegerField()
    saves = models.IntegerField()
    clean_sheets = models.IntegerField()
    issued_card = models.IntegerField()
    date = models.DateField()

    assister = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='assists_provided', null=True, blank=True)
    goalscorer = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='goals_scored', null=True, blank=True)
    cardgiven = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='cards_given', null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)