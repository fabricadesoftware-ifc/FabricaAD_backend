from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .models import Usuario
from .serializers import UsuarioSerializer
from filters import EmployerFilter


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployerFilter
    

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and not user.is_superuser:
            user_data = Usuario.objects.get(email=user)
            return Usuario.objects.filter(enterprise=user_data.enterprise)
        return Usuario.objects.all()

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def me(self, req):
        user = req.user
        serializer = UsuarioSerializer(user)    
        return Response(data=serializer.data, status=status.HTTP_200_OK)

