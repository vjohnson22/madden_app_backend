from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('owners/', views.OwnerList.as_view(), name='owner_list'),
    path('owners/<int:pk>', views.OwnerDetail.as_view(), name='owner_detail'),
    path('games/', views.GameList.as_view(), name='game_list'),
    path('games/<int:pk>', views.GameDetail.as_view(), name='game_detail'),
    path('gamestats/', views.GameStatList.as_view(), name='game_stats_list'),
    path('gamestats/<int:pk>', views.GameStatDetail.as_view(), name='game_stats_detail'),
    path('players/', views.PlayerList.as_view(), name='player_list'),
    path('players/<int:pk>', views.PlayerDetail.as_view(), name='player_detail'),
    path('playerstats/', views.PlayerStatList.as_view(), name='player_stats_list'),
    path('playerstats/<int:pk>', views.PlayerStatDetail.as_view(), name='player_stats_detail')

]