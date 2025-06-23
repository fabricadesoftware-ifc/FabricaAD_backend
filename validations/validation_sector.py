from rest_framework.serializers import ValidationError
from core.models import Sector

def validate_sector(attrs):
    errors = {}

    name = attrs.get('name')
    description = attrs.get('description')
    enterprise = attrs.get('enterprise')

    if not name:
        errors['name'] = ['O nome do setor não pode ser vazio.']
    else:
        if len(name) > 40:
            errors.setdefault('name', []).append('O nome do setor deve ter no máximo 40 caracteres.')
        if Sector.objects.filter(name=name).exists():
            errors.setdefault('name', []).append('Já existe um setor com esse nome.')

    if not enterprise:
        errors['enterprise'] = ['O setor precisa estar associado a uma empresa.']

    if description and len(description) > 500:
        errors.setdefault('description', []).append('A descrição deve ter no máximo 500 caracteres.')

    if errors:
        raise serializers.ValidationError(errors)

    return attrs
