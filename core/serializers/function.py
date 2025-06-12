from core.models import Function, Position, Sector
from rest_framework.serializers import ModelSerializer, SlugRelatedField,PrimaryKeyRelatedField, ValidationError
from usuario.serializers import UsuarioInfoSerializer
from usuario.models import Usuario as User
from core.serializers.sector import SectorSerializer
from validations import validate_function

class FunctionCreateSerializer(ModelSerializer):
    employer = UsuarioInfoSerializer(read_only=True)
    employer_registration = SlugRelatedField(slug_field='registration', write_only=True, queryset=User.objects.all(), allow_null=True)
    supervisor = UsuarioInfoSerializer(read_only=True)
    supervisor_registration = SlugRelatedField(slug_field='registration', write_only=True, queryset=User.objects.all(), allow_null=True)
    position = SlugRelatedField(slug_field='name', queryset=Position.objects.all(), validators=[], allow_null=True)
    sector = SectorSerializer(read_only=True)
    sector_id = PrimaryKeyRelatedField(
        source='sector',
        queryset=Sector.objects.all(),
        write_only=True,
        allow_null=True
    )
    class Meta:
        model = Function
        fields = [
            'id',
            'employer', 'employer_registration',
            'supervisor', 'supervisor_registration',
            'position',
            'sector', 'sector_id',
        ]

    def create(self, validated_data):
        employer = validated_data.pop('employer_registration', None)
        supervisor = validated_data.pop('supervisor_registration', None)

        validated_data['employer'] = employer
        validated_data['supervisor'] = supervisor

        return Function.objects.create(**validated_data)
    
    def validate(self, attrs):
        validate_function(attrs)
        return super().validate(attrs)


class FunctionSerializer(ModelSerializer):
    class Meta:
        model = Function
        fields = '__all__'
        depth = 1