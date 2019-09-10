from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Game(models.Model):
    season = models.PositiveIntegerField()
    week = models.PositiveIntegerField()
    won = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='wins')
    lost = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='losses')

    def __str__(self):
        return f'{self.won} vs {self.lost}: Week {self.week}, {self.season}'

class GameStat(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_stats')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner_game_stats')
    against = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='played_against')
    # season = models.PositiveIntegerField(default=2019)
    # week = models.PositiveIntegerField(default = 0)
    points = models.PositiveIntegerField()
    off_yards_gained = models.PositiveIntegerField()
    rush_yards = models.PositiveIntegerField()
    pass_yards = models.PositiveIntegerField()
    first_downs = models.PositiveIntegerField()
    punt_return_yards = models.PositiveIntegerField()
    kick_return_yards = models.PositiveIntegerField()
    turnovers = models.PositiveIntegerField(default=0)

    
class Player(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()
    position = models.CharField(max_length=2, default=0)

    def __str__(self):
        return self.name


class PlayerStat(models.Model):
    name = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='player_owner')
    against = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner_played_against')
    pass_yards = models.PositiveIntegerField(default=0)
    pass_td = models.PositiveIntegerField(default=0)
    pass_int = models.PositiveIntegerField(default=0)
    times_sacked = models.PositiveIntegerField(default=0)
    pass_complete = models.PositiveIntegerField(default=0)
    pass_attempt  = models.PositiveIntegerField(default=0)
    rush_yards = models.PositiveIntegerField(default=0)
    rush_tds = models.PositiveIntegerField(default=0)
    fumbled = models.PositiveIntegerField(default=0)
    break_tackle = models.PositiveIntegerField(default=0) 
    receptions = models.PositiveIntegerField(default=0)
    receiving_yards =models.PositiveIntegerField( default=0)
    receiving_tds = models.PositiveIntegerField( default=0)
    tackles = models.PositiveIntegerField(default=0)
    tfl = models.PositiveIntegerField(default=0)
    sacks = models.PositiveIntegerField(default=0)
    interceptions = models.PositiveIntegerField(default=0)
    defensive_tds = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.name}: {self.game}'

class SeasonStat(models.Model):
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

    def __str__(self):
        return f'{self.owner}: {self.season} Season'