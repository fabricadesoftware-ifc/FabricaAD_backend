from core.models import Avaliation
from rest_framework.serializers import ModelSerializer

class AvaliationSerializer(ModelSerializer):
    class Meta:
        model = Avaliation
        fields = '__all__'
        depth = 1
