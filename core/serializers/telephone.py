from rest_framework.serializers import ModelSerializer, SlugRelatedField
from validations.validation_telephone import validate_telephone

from core.models import Telephone
from usuario.models import Usuario as User
from core.models.enterprise import Enterprise

class TelephoneSerializer(ModelSerializer):
    user_phone = SlugRelatedField(
        slug_field='email',
        queryset=User.objects.all(),
        allow_null=True,
        required=False
    )
    enterprise_phone = SlugRelatedField(
        slug_field='name',
        queryset=Enterprise.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Telephone
        fields = "__all__"

    def validate(self, attrs):
        validate_telephone(attrs)
        return attrs
