from core.models import Telephone
from core.serializers import TelephoneSerializer
from rest_framework.viewsets import ModelViewSet

class TelephoneViewSet(ModelViewSet):
    queryset = Telephone.objects.all()
    serializer_class = TelephoneSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and not user.is_superuser:
            return Telephone.objects.filter(user_phone=user)
        return Telephone.objects.all()