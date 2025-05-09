from core.models import Function
from core.serializers import FunctionCreateSerializer, FunctionSerializer
from rest_framework.viewsets import ModelViewSet

class FunctionViewSet(ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return FunctionCreateSerializer
        return FunctionSerializer