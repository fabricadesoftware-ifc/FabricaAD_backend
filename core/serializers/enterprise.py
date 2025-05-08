from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Enterprise

class EnterpriseSerializer(ModelSerializer):
    class Meta:
        model = Enterprise
        fields = __all__
        