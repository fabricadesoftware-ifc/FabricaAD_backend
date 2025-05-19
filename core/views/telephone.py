from core.models import Telephone
from core.serializers import TelephoneSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from filters import TelephoneFilter

class TelephoneViewSet(ModelViewSet):
    queryset = Telephone.objects.all()
    serializer_class = TelephoneSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    authentication_classes = [JWTAuthentication]
    filterset_class = TelephoneFilter


    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and not user.is_superuser:
            return Telephone.objects.filter(user_phone=user)
        return Telephone.objects.all()