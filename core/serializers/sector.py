from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Sector, Enterprise

class SectorSerializer(ModelSerializer):
    enterprise = SlugRelatedField(slug_field='name', queryset=Enterprise.objects.all())
    class Meta:
        model = Sector
        fields = "__all__"