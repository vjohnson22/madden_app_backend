from rest_framework import serializers
from .models import Game, Owner, GameStat, Player, PlayerStat, SeasonStat 



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
    seasons = serializers.HyperlinkedRelatedField(
        view_name='season_stats_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Owner
        fields = ('id','name', 'photo_url', 'wins', 'losses','owner_game_stats','played_against', 'seasons')

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
    players_game_stats = serializers.HyperlinkedRelatedField(
        view_name='owner_detail',
        many= True,
        read_only=True
    )

    class Meta:
        model = Game
        fields = ('id','season', 'week', 'won', 'lost', 'game_stats','players_game_stats')

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

class PlayerStatSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        read_only=True
    )
    game = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        read_only=True
    )
    owner = serializers.HyperlinkedRelatedField(
        view_name='owner_detail',
        read_only=True
    )
    against  = serializers.HyperlinkedRelatedField(
        view_name='owner_detail',
        read_only=True
    )

    class Meta:
        model = PlayerStat
        fields = ('id','name', 'game','owner','against','pass_yards','pass_td',  'pass_int','times_sacked', 'pass_complete','pass_attempt','rush_yards','rush_tds','fumbled','break_tackle','receptions','receiving_yards', 'receiving_tds','tackles','tfl','sacks','interceptions','defensive_tds')

class SeasonStatSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        view_name='owner_detail',
        read_only=True
    )
    class Meta:
        model = SeasonStat
        fields = ('id','owner', 'season','wins','losses','pf','pa','total_yards_offense','total_offense','pass_yards','rush_yards','ppg', 'pass_tds','rush_tds','first_downs','total_yards_defense','pass_yards_allowed','rush_yards_allowed','sacks', 'forced_fumbles',   'interceptions')
