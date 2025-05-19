from core.models import Sector
from core.serializers import SectorSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from usuario.models import Usuario as User
from django_filters.rest_framework import DjangoFilterBackend
from filters import SectorFilter

class SectorViewSet(ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SectorFilter

    def get_queryset(self):
        user = self.request.user 

        user_data = User.objects.get(email=user)

        if user.is_authenticated and not user.is_superuser:
            return Sector.objects.filter(enterprise=user_data.enterprise)
        return Sector.objects.all()