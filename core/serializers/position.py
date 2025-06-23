from core.models import Position
from rest_framework.serializers import ModelSerializer
from validations.validation_position import validate_position

class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        depth = 1

    def validate(self, attrs):
        validate_position(attrs)
        return attrs