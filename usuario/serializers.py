from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.hashers import make_password
from .models import Usuario
from core.models.telephone import Telephone
from core.serializers.telephone import TelephoneSerializer
from validations.validation_employer import validate_employer
from rest_framework.serializers import ValidationError

class UsuarioSerializer(ModelSerializer):
    telephones = TelephoneSerializer(many=True, required=False)
    registration = CharField(required=False, allow_blank=True, validators=[])
    email = CharField(required=False, allow_blank=True, allow_null=True,validators=[])
    password = CharField(required=False, allow_blank=True, allow_null=True, validators=[])
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'password', 'registration', 'enterprise', "telephones", 'first_name', 'last_name']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        telephones = validated_data.pop("telephones", [])

        user = super().create(validated_data)
    
        if len(telephones) > 0:
            for telephone in telephones:
                print(telephone, telephones)
                Telephone.objects.create(user_phone=user, **telephone)

        return user

    def validate(self, attrs):
        validate_employer(attrs)
        return super().validate(attrs)

class UsuarioInfoSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'first_name', 'last_name', 'registration', 'enterprise']