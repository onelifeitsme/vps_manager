from django.urls import path
from . import views


urlpatterns = [
    path('vps/', views.VSPAPIView.as_view()),
    path('vps/<uuid:pk>/', views.SingleVPSAPIView.as_view()),
]
