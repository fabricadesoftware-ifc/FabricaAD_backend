from core.models import Function, Position, Sector, Enterprise
from rest_framework.serializers import ModelSerializer, SlugRelatedField,PrimaryKeyRelatedField
from usuario.serializers import UsuarioSerializer
from usuario.models import Usuario as User
from core.serializers.sector import SectorSerializer


class FunctionCreateSerializer(ModelSerializer):
    employer = UsuarioSerializer()
    supervisor = SlugRelatedField(slug_field='registration', queryset=User.objects.all())
    position = SlugRelatedField(slug_field='name', queryset=Position.objects.all())
    sector = SectorSerializer(read_only=True)
    sector_id = PrimaryKeyRelatedField(
        source='sector',
        queryset=Sector.objects.all(),
        write_only=True
    )
    class Meta:
        model = Function
        fields = '__all__'

    def create(self, validated_data):
        employer_obj = validated_data.pop('employer')

        enterprise_id = employer_obj['enterprise'].id

        employer_obj['enterprise'] = enterprise_id

        employer_serializer = UsuarioSerializer(data=employer_obj)
        employer_serializer.is_valid(raise_exception=True)
        employer = employer_serializer.save()

        function = Function.objects.create(
            employer=employer,
            **validated_data
        )

        return function

class FunctionSerializer(ModelSerializer):
    class Meta:
        model = Function
        fields = '__all__'
        depth = 1

    

    