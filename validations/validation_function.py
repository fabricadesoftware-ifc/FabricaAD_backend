from rest_framework.serializers import ValidationError
from usuario.models import Usuario as User

def validate_function(attrs):
    supervisor = attrs.get('supervisor_registration')
    sector = attrs.get('sector')
    position = attrs.get('position')
    employer = attrs.get('employer_registration')

    errors = {}

    if not supervisor:
        errors['supervisor'] = ['o campo de supervisor precisa de ser preenchido']

    if not sector:
        errors['sector'] = ['o campo de setor precisa de ser preenchido']

    if not position:
        errors['position'] = ['o campo de cargo precisa de ser preenchido']

    if not employer:
        errors['employer'] = ['o campo de funcionário precisa de ser preenchido']

    if errors:
        raise ValidationError(errors)

    return attrs

     
