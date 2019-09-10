from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import OwnerSerializer, GameSerializer, GameStatSerializer
from .models import Game, Owner, GameStat

#  GameStat, Player, PlayerStat, SeasonStat

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