from core.models import Position
from core.serializers import PositionSerializer
from rest_framework.viewsets import ModelViewSet

class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer