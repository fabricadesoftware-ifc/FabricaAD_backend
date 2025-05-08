from usuario.models import Employer
from usuario.serializers import EmployerCreateSerializer, EmployerSerializer
from rest_framework.viewsets import ModelViewSet

class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return EmployerCreateSerializer
        return EmployerSerializer