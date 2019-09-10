from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import OwnerSerializer, GameSerializer, GameStatSerializer, PlayerSerializer, PlayerStatSerializer
from .models import Game, Owner, GameStat, Player, PlayerStat

#  SeasonStat

class OwnerList(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer    

class GameStatList(generics.ListCreateAPIView):
    queryset = GameStat.objects.all()
    serializer_class = GameStatSerializer

class GameStatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameStat.objects.all()
    serializer_class = GameStatSerializer    

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer    

class PlayerStatList(generics.ListCreateAPIView):
    queryset = PlayerStat.objects.all()
    serializer_class = PlayerStatSerializer

class PlayerStatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerStat.objects.all()
    serializer_class = PlayerStatSerializer    