from rest_framework import serializers
from core.models import Enterprise

def validate_enterprise(attrs):
    errors = {}

    name = attrs.get('name')
    fantasy_name = attrs.get('fantasy_name')

    if not name:
        errors['name'] = ['O campo "name" não pode ser vazio.']
    else:
        name = name.strip()
        if Enterprise.objects.filter(name=name).exists():
            errors.setdefault('name', []).append('O nome da empresa já está cadastrado.')
            if len(name) > 40:
                errors.setdefault('name', []).append('O nome da empresa não pode ter mais de 40 caracteres.')
    
    if not fantasy_name:
        errors['fantasy_name'] = ['O campo "fantasy_name" não pode ser vazio.']
    else:
        fantasy_name = fantasy_name.strip()
        if Enterprise.objects.filter(fantasy_name=fantasy_name).exists():
            errors.setdefault('fantasy_name', []).append('Esse nome fantasia já está cadastrado.')
    
    if errors:
        raise serializers.ValidationError(errors)
    
    return attrs