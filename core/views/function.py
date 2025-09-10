from core.models import Function
from core.models import Avaliation
from core.serializers import FunctionCreateSerializer, FunctionSerializer, AvaliationSerializer
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
    def subordinates(self, request):
        avaliation = []
        user = request.user
        supervisor = Function.objects.filter(supervisor=user)
        avaliation = Avaliation.objects.filter(evaluator=user)
        avaliation_serializer = AvaliationSerializer(avaliation, many=True)
        serializer = FunctionSerializer(supervisor, many=True)
        avaliation = [item['avaliation_is_in_day'] for item in avaliation_serializer.data]
        
        for idx, i in enumerate(serializer.data):
            i['avaliation_is_in_day'] = avaliation[idx]

        return Response({
            "user_function": [{
                "email": item['employer']['email'],
                "name": item['employer']['first_name'] + '' + item['employer']['last_name'],
                "registration": item['employer']['registration'],
                "media": item['employer']['media'],
                "sector": item['sector']['name'],
                "avaliation": item['avaliation_is_in_day']
            } for item in serializer.data] }, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly], authentication_classes=[JWTAuthentication])
    def myteam(self, request):
        user = request.user
        my_function = Function.objects.filter(employer=user)
        my_team = Function.objects.filter(supervisor=my_function.supervisor)
        serializer = FunctionSerializer(my_team, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
