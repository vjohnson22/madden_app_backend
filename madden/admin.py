from django.contrib import admin
from .models import Game, GameStat, Owner, Player, PlayerStat, SeasonStat
# Register your models here.

admin.site.register(Game)
admin.site.register(GameStat)
admin.site.register(Owner)
admin.site.register(Player)
admin.site.register(PlayerStat)
admin.site.register(SeasonStat)