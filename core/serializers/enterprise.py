from rest_framework.serializers import ModelSerializer, SlugRelatedField
from validations.validation_enterprise import validate_enterprise

from core.models import Enterprise

class EnterpriseSerializer(ModelSerializer):
    class Meta:
        model = Enterprise
        fields = "__all__"
    
    def validate(self, attrs):
        validate_enterprise(attrs)
        return attrs