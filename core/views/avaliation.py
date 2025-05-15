from core.models import Avaliation
from core.serializers import AvaliationSerializer, AvaliationCreateSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

class AvaliationViewSet(ModelViewSet):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication] 

    def get_queryset(self):
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return Avaliation.objects.filter(evaluated=self.request.user)
        return Avaliation.objects.all()

    def get_serializer_class(self, **kwargs):
        if self.action == 'create':
            return AvaliationCreateSerializer
        return AvaliationSerializer
    
