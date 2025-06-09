from rest_framework import serializers
from core.models import Position

def validate_position(attrs):
    errors = {}

    name = attrs.get('name')

    if not name:
        errors['name'] = ['O nome da posição não pode ser vazio.']
    else:
        normalized_name = name.strip().lower()
        if Position.objects.filter(name__iexact=normalized_name).exists():
            errors.setdefault('name', []).append('Essa posição já existe.')
    if errors:
        raise serializers.ValidationError(errors)


    return attrs
    