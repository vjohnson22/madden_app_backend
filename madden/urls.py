from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('owners/', views.OwnerList.as_view(), name='owner_list'),
    path('owners/<int:pk>', views.OwnerDetail.as_view(), name='owner_detail'),
]