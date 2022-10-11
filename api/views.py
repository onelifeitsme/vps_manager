from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import BasicVPSSerializer, FullVPSSerializer
from vps.models import VPS


class VSPAPIView(ListCreateAPIView):
    queryset = VPS.objects.all()
    serializer_class = FullVPSSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('cpu', 'ram', 'hdd', 'status',)


class SingleVPSAPIView(RetrieveUpdateAPIView):
    queryset = VPS.objects.all()
    serializer_class = BasicVPSSerializer
