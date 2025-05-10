from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Sector, Enterprise

class SectorSerializer(ModelSerializer):
    enterprise = SlugRelatedField(
        queryset=Enterprise.objects.all(),
        slug_field='name_enterprise'
    )
    class Meta:
        model = Sector
        fields = "__all__"