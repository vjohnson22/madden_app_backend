from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('owners/', views.OwnerList.as_view(), name='owner_list'),
    path('owners/<int:pk>', views.OwnerDetail.as_view(), name='owner_detail'),
    path('games/', views.GameList.as_view(), name='game_list'),
    path('games/<int:pk>', views.GameDetail.as_view(), name='game_detail'),
    path('gamestats/', views.GameStatList.as_view(), name='game_stats_list'),
    path('gamestats/<int:pk>', views.GameStatDetail.as_view(), name='game_stats_detail')

]