from rest_framework import serializers
from .models import Game, Owner, GameStat, Player 

#  PlayerStat, SeasonStat

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    wins = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        many=True,
        read_only=True
    )
    losses = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        many=True,
        read_only=True
    )
    owner_game_stats = serializers.HyperlinkedRelatedField(
        view_name='game_stats_detail',
        many=True,
        read_only=True
    )
    played_against = serializers.HyperlinkedRelatedField(
        view_name='game_stats_detail',
        many=True,
        read_only=True
    )
    # played_against = serializers.HyperlinkedRelatedField(
    #     view_name='played_against_detail',
    #     many=True,
    #     read_only=True
    # )
    # player_owner = serializers.HyperlinkedRelatedField(
    #     view_name='player_owner_detail',
    #     many=True,
    #     read_only=True
    # )
    # owner_played_against = serializers.HyperlinkedRelatedField(
    #     view_name='owner_played_against_detail',
    #     many=True,
    #     read_only=True
    # )
    # season_owner = serializers.HyperlinkedRelatedField(
    #     view_name='season_owner_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Owner
        fields = ('id','name', 'photo_url', 'wins', 'losses','owner_game_stats','played_against')

        # 'owner_game_stats','played_against','player_owner','owner_played_against', 'season_owner'

class GameSerializer(serializers.HyperlinkedModelSerializer):
    won = serializers.HyperlinkedRelatedField(
        view_name='owner_detail',
        read_only=True
    )
    lost = serializers.HyperlinkedRelatedField(
        view_name='owner_detail',
        read_only=True
    )
    game_stats = serializers.HyperlinkedRelatedField(
        view_name='game_stats_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Game
        fields = ('id','season', 'week', 'won', 'lost', 'game_stats')

class GameStatSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        read_only=True
    )
    owner = serializers.HyperlinkedRelatedField(
        view_name='owner_detail',
        read_only=True
    )
    against = serializers.HyperlinkedRelatedField(
        view_name='owner_detail',
        read_only=True
    )

    class Meta:
        model = GameStat
        fields = ('id','game','owner','against','points','off_yards_gained','rush_yards', 'pass_yards','first_downs','punt_return_yards','kick_return_yards','turnovers')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    player_stats = serializers.HyperlinkedRelatedField(
        view_name='player_stats_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Player
        fields = ('id','name', 'photo_url','position','player_stats')
