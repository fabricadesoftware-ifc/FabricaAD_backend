from rest_framework import serializers
from core.models import Position
import unicodedata

def normalize(text):
    if not text:
        return ''
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if not unicodedata.combining(c)
    ).lower()

def validate_position(attrs):
    errors = {}

    name = attrs.get('name')
    description = attrs.get('description')

    if not name:
        errors['name'] = ['O nome da posição não pode ser vazio.']
    else:
        name = name.strip()
        normalized_name = normalize(name)
        for pos in Position.objects.all():
            if normalize(pos.name) == normalized_name:
                errors.setdefault('name', []).append('Já existe uma posição com esse nome.')

    if not description:
        errors['description'] = ['A descrição da posição não pode ser vazia.']
    
    
    if errors:
        raise serializers.ValidationError(errors)
  
    return attrs
    