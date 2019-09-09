from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

class Game(models.Model):
    season = models.PositiveIntegerField(max_length=4)
    week = models.PositiveIntegerField(max_length=2)
    won = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='wins')
    lost = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='losses')

class GameStats(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='gameStats')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner')
    against = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='against')
    points = models.PositiveIntegerField(max_length = 3)
    off_yards_gained = models.PositiveIntegerField(max_length = 4)
    rush_yards = models.PositiveIntegerField(max_length = 4)
    pass_yards = models.PositiveIntegerField(max_length = 4)
    first_downs = models.PositiveIntegerField(max_length = 3)
    punt_return_yards = models.PositiveIntegerField(max_length = 4)
    kick_return_yards = models.PositiveIntegerField(max_length = 4)

class Player(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

class PlayerStats(models.Model):
    name = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player')
    position = models.CharField(max_length= 2)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner')
    against = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner')
    pass_yards = models.PositiveIntegerField(max_length = 4, blank=True)
    pass_td = models.PositiveIntegerField(max_length = 2, blank=True)
    pass_int = models.PositiveIntegerField(max_length = 2, blank=True)
    times_sacked = models.PositiveIntegerField(max_length = 2, blank=True)
    pass_complete = models.PositiveIntegerField(max_length = 2, blank=True)
    pass_attempt  = models.PositiveIntegerField(max_length = 2, blank=True)
    rush_yards = models.PositiveIntegerField(max_length = 4, blank=True)
    rush_tds = models.PositiveIntegerField(max_length = 2, blank=True)
    fumbled = models.PositiveIntegerField(max_length = 2, blank=True)
    break_tackle = models.PositiveIntegerField(max_length = 2, blank=True) 
    receptions = models.PositiveIntegerField(max_length = 2, blank=True)
    receiving_yards =models.PositiveIntegerField(max_length = 4, blank=True)
    receiving_tds = models.PositiveIntegerField(max_length = 2, blank=True)
    tackles = models.PositiveIntegerField(max_length = 2, blank=True)
    tfl = models.PositiveIntegerField(max_length = 3, blank=True)
    sacks = models.PositiveIntegerField(max_length = 2, blank=True)
    interceptions = models.PositiveIntegerField(max_length = 2, blank=True)
    defensive_tds = models.PositiveIntegerField(max_length = 2, blank=True)

class SeasonStats(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner')
    season = models.PositiveIntegerField(max_length = 4) 
    wins = models.PositiveIntegerField(max_length = 2)
    losses = models.PositiveIntegerField(max_length = 2)
    pf = models.PositiveIntegerField(max_length = 4)
    pa = models.PositiveIntegerField(max_length = 4)
    total_yards_offense = models.PositiveIntegerField(max_length = 5) 
    total_offense = models.PositiveIntegerField(max_length = 5)
    pass_yards = models.PositiveIntegerField(max_length = 5)
    rush_yards = models.PositiveIntegerField(max_length = 5)
    ppg = models.FloatField(max_length = 3)
    pass_tds = models.PositiveIntegerField(max_length = 3)
    rush_tds = models.PositiveIntegerField(max_length = 3)
    first_downs = models.PositiveIntegerField(max_length = 4)
    total_yards_defense = models.PositiveIntegerField(max_length = 5)
    pass_yards_allowed = models.PositiveIntegerField(max_length = 5)
    rush_yards_allowed = models.PositiveIntegerField(max_length = 5)
    sacks = models.PositiveIntegerField(max_length = 3)
    forced_fumbles = models.PositiveIntegerField(max_length = 3)
    interceptions = models.PositiveIntegerField(max_length = 3)

