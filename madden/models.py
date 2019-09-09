from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

class Game(models.Model):
    season = models.PositiveIntegerField()
    week = models.PositiveIntegerField()
    won = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='wins')
    lost = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='losses')

class GameStats(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_stats')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner_game_Stats')
    against = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='played_against')
    points = models.PositiveIntegerField()
    off_yards_gained = models.PositiveIntegerField()
    rush_yards = models.PositiveIntegerField()
    pass_yards = models.PositiveIntegerField()
    first_downs = models.PositiveIntegerField()
    punt_return_yards = models.PositiveIntegerField()
    kick_return_yards = models.PositiveIntegerField()

class Player(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

class PlayerStats(models.Model):
    name = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player')
    position = models.CharField(max_length= 2)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='player_owner')
    against = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner_played_against')
    pass_yards = models.PositiveIntegerField(blank=True)
    pass_td = models.PositiveIntegerField(blank=True)
    pass_int = models.PositiveIntegerField(blank=True)
    times_sacked = models.PositiveIntegerField(blank=True)
    pass_complete = models.PositiveIntegerField(blank=True)
    pass_attempt  = models.PositiveIntegerField(blank=True)
    rush_yards = models.PositiveIntegerField(blank=True)
    rush_tds = models.PositiveIntegerField(blank=True)
    fumbled = models.PositiveIntegerField(blank=True)
    break_tackle = models.PositiveIntegerField(blank=True) 
    receptions = models.PositiveIntegerField(blank=True)
    receiving_yards =models.PositiveIntegerField( blank=True)
    receiving_tds = models.PositiveIntegerField( blank=True)
    tackles = models.PositiveIntegerField(blank=True)
    tfl = models.PositiveIntegerField(blank=True)
    sacks = models.PositiveIntegerField(blank=True)
    interceptions = models.PositiveIntegerField(blank=True)
    defensive_tds = models.PositiveIntegerField(blank=True)

class SeasonStats(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='season_owner')
    season = models.PositiveIntegerField() 
    wins = models.PositiveIntegerField()
    losses = models.PositiveIntegerField()
    pf = models.PositiveIntegerField()
    pa = models.PositiveIntegerField()
    total_yards_offense = models.PositiveIntegerField() 
    total_offense = models.PositiveIntegerField()
    pass_yards = models.PositiveIntegerField()
    rush_yards = models.PositiveIntegerField()
    ppg = models.FloatField()
    pass_tds = models.PositiveIntegerField()
    rush_tds = models.PositiveIntegerField()
    first_downs = models.PositiveIntegerField()
    total_yards_defense = models.PositiveIntegerField()
    pass_yards_allowed = models.PositiveIntegerField()
    rush_yards_allowed = models.PositiveIntegerField()
    sacks = models.PositiveIntegerField()
    forced_fumbles = models.PositiveIntegerField()
    interceptions = models.PositiveIntegerField()

