from rest_framework import serializers
from vps.models import VPS


class VPSSerializer(serializers.ModelSerializer):

    class Meta:
        model = VPS
        fields = '__all__'
        extra_kwargs = {
            'cpu': {"read_only": True},
            'ram': {"read_only": True},
            'hdd': {"read_only": True},
        }