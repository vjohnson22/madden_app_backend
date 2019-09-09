from rest_framework import serializers
from .models import Game, GameStat, Owner, Player, PlayerStat, SeasonStat

class GameSerializer(serializers.HyperlinkedModelSerializer):
    wins = serializers.HyperlinkedRelatedField(
        view_name='win_detail',
        many=True,
        read_only=True
    )
    losses = serializers.HyperlinkedRelatedField(
        view_name='loss_detail',
        many=True,
        read_only=True
    )
    owner_game_stats = serializers.HyperlinkedRelatedField(
        view_name='win_detail',
        many=True,
        read_only=True
    )
    played_against = serializers.HyperlinkedRelatedField(
        view_name='win_detail',
        many=True,
        read_only=True
    )
    player_owner = serializers.HyperlinkedRelatedField(
        view_name='win_detail',
        many=True,
        read_only=True
    )
    owner_played_against = serializers.HyperlinkedRelatedField(
        view_name='win_detail',
        many=True,
        read_only=True
    )
    season_owner = serializers.HyperlinkedRelatedField(
        view_name='win_detail',
        many=True,
        read_only=True
    )