from rest_framework.serializers import ModelSerializer

from core.models import Sector

class SectorSerializer(ModelSerializer):
    class Meta:
        model = Sector
        fields = __all__