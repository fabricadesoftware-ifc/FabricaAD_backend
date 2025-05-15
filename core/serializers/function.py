from core.models import Function, Position
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from usuario.models import Usuario as User
from usuario.serializers import UsuarioInfoAvaliationSerializer

class FunctionCreateSerializer(ModelSerializer):
    employer = UsuarioInfoAvaliationSerializer()
    supervisor = UsuarioInfoAvaliationSerializer()
    position = SlugRelatedField(slug_field='name', queryset=Position.objects.all())
    class Meta:
        model = Function
        fields = '__all__'

class FunctionSerializer(ModelSerializer):
    class Meta:
        model = Function
        fields = '__all__'
        depth = 1

    

    