from core.models import Avaliation
from core.serializers import AvaliationSerializer, AvaliationCreateSerializer
from rest_framework.viewsets import ModelViewSet

class AvaliationViewSet(ModelViewSet):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def get_serializer_class(self, **kwargs):
        if self.action == 'create':
            return AvaliationCreateSerializer
        return AvaliationSerializer