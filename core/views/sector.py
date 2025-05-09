from core.models import Sector
from core.serializers import SectorSerializer
from rest_framework.viewsets import ModelViewSet

class SectorViewSet(ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer