from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Sector, Enterprise
from validations import validate_sector

class SectorSerializer(ModelSerializer):
    enterprise = SlugRelatedField(slug_field='name', queryset=Enterprise.objects.all())
    class Meta:
        model = Sector
        fields = "__all__"

    def validate(self, attrs):
        return validate_sector(attrs)
    
