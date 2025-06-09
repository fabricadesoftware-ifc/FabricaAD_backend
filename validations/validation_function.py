from rest_framework.serializers import ValidationError
def validate_function(attrs):
    supervisor = attrs.get('supervisor')
    sector = attrs.get('sector')
    position = attrs.get('position')

    errors = {}

    if not supervisor:
        errors['supervisor'] = ['o campo de supervisor é precisa de ser preenchido'] 

    if not sector:
        errors['sector'] = ['o campo de setor precisa de ser preenchido']

    if not position:
        errors['position'] = ['o campo de cargo precisa de ser preenchido']

    if errors:
        raise ValidationError(errors)

    return attrs

     
