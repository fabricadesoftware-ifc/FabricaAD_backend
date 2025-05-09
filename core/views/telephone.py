from core.models import Telephone
from core.serializers import TelephoneSerializer
from rest_framework.viewsets import ModelViewSet

class TelephoneViewSet(ModelViewSet):
    queryset = Telephone.objects.all()
    serializer_class = TelephoneSerializer