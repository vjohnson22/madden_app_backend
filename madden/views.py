from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import OwnerSerializer
from .models import Game, GameStat, Owner, Player, PlayerStat, SeasonStat

class OwnerList(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer