from django.urls import path
from . import views


urlpatterns = [
    path('vps/', views.VSPAPIView.as_view(), name='vps_list'),
    path('vps/<uuid:pk>/', views.SingleVPSAPIView.as_view(), name='vps_detail'),
]
