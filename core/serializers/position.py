from core.models import Position
from rest_framework.serializers import ModelSerializer

class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        depth = 1