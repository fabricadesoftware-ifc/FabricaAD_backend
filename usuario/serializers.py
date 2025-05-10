from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import Usuario
from core.models.telephone import Telephone
from core.serializers.telephone import TelephoneSerializer


class UsuarioSerializer(ModelSerializer):
    telephones = TelephoneSerializer(many=True, required=False)
    
    class Meta:
        model = Usuario
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        validated_data['password'] = make_password(validated_data['password'])
        telephones = validated_data.pop("telephones", [])
        print(telephones)

        user = super().create(validated_data)

        if len(telephones) > 0:
            for telephone in telephones:
                print(telephone, telephones)
                Telephone.objects.create(user_phone=user, **telephone)

        return user


    
    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return validated_data