from core.models import Function, Position, Sector
from rest_framework.serializers import ModelSerializer, SlugRelatedField,PrimaryKeyRelatedField, ValidationError
from usuario.serializers import UsuarioSerializer
from usuario.models import Usuario as User
from core.serializers.sector import SectorSerializer
from validations import validate_function, validate_employer

class FunctionCreateSerializer(ModelSerializer):
    employer = UsuarioSerializer()
    supervisor = SlugRelatedField(slug_field='registration', queryset=User.objects.all(), validators=[], allow_null=True)
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

    def validate(self, attrs):
        errors = {}
        employer_data = attrs.get('employer')

        try:
            validate_function(attrs)
        except ValidationError as e:
            errors.update(e.detail)

        try: 
            validate_employer(employer_data)
        except ValidationError as e:
            errors['employer'] = e.detail
        
        if errors:
            raise ValidationError(errors)

        return super().validate(attrs)


class FunctionSerializer(ModelSerializer):
    class Meta:
        model = Function
        fields = '__all__'
        depth = 1


    

    