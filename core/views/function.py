from core.models import Function
from core.serializers import FunctionCreateSerializer, FunctionSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

class FunctionViewSet(ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return FunctionCreateSerializer
        return FunctionSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly], authentication_classes=[JWTAuthentication])
    def leader(self, request):
        user = request.user
        supervisor = Function.objects.filter(supervisor=user)
        serializer = FunctionSerializer(supervisor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly], authentication_classes=[JWTAuthentication])
    def my_team(self, request):
        user = request.user
        my_function = Function.objects.get(employer=user)
        my_team = Function.objects.filter(supervisor=my_function.supervisor)
        serializer = FunctionSerializer(my_team, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
