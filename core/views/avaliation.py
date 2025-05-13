from core.models import Avaliation
from core.serializers import AvaliationSerializer
from rest_framework.viewsets import ModelViewSet

class AvaliationViewSet(ModelViewSet):
    
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer