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
    date = models.DateField()
class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Making sure each player has a unique name
    assists = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    shutouts = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)

    def __str__(self):
        return self.name

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.assister:
            self.assister.assists += 1
            self.assister.save()
        if self.goalscorer:
            self.goalscorer.goals += 1
            self.goalscorer.save()
        if self.red_card:
            self.red_card.red_cards += 1
            self.red_card.save()
        if self.yellow_card:
            self.yellow_card.yellow_cards += 1
            self.yellow_card.save()
        if self.shutouts:
            self.shutouts.shutouts += 1
            self.shutouts.save()
        if self.savers:
            self.savers.saves += self.saves if self.saves else 0
            self.savers.save()

    def __str__(self):
        return f"{self.user.username} vs {self.vs} on {self.date}"