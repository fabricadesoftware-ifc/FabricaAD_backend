from core.models import Function, Position
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from usuario.models import Employer

class FunctionCreateSerializer(ModelSerializer):
    employer = SlugRelatedField(slug_field='registration', queryset=Employer.objects.all())
    supervisor = SlugRelatedField(slug_field='registration', queryset=Employer.objects.all())
    position = SlugRelatedField(slug_field='name', queryset=Position.objects.all())
    class Meta:
        model = Function
        fields = '__all__'

class FunctionSerializer(ModelSerializer):
    class Meta:
        model = Function
        fields = '__all__'
        depth = 1

    

    