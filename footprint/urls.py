from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('footprint/', views.FootprintList.as_view(), name='footprint_list'),
    path('footprint/<int:pk>', views.FootprintDetail.as_view(), name='footprint_detail')
]