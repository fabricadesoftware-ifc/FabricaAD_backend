from rest_framework.serializers import ModelSerializer
from usuario.models import Employer, Usuario
from usuario.serializers import UsuarioSerializer

class EmployerCreateSerializer(ModelSerializer):
    user = UsuarioSerializer()
    class Meta:
        model = Employer
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data.pop('user')
        user_data = Usuario.objects.create(user)
        employer = Employer.objects.create(user=user_data, **validated_data)
        return employer

class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
        depth = 1