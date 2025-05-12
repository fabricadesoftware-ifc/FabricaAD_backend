from rest_framework.serializers import ModelSerializer
from core.models import Sector
from core.serializers import EnterpriseSerializer

class SectorSerializer(ModelSerializer):
    enterprise = EnterpriseSerializer()
    class Meta:
        model = Sector
        fields = "__all__"