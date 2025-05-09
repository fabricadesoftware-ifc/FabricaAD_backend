from core.models import Enterprise
from core.serializers import EnterpriseSerializer
from rest_framework.viewsets import ModelViewSet

class EnterpriseViewSet(ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
