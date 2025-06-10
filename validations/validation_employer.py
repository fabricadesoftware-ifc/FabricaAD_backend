from rest_framework import serializers
from usuario.models import Usuario as User
def validate_employer(attrs):
    errors = {}

    first_name = attrs.get('first_name')
    last_name = attrs.get('last_name')
    enterprise = attrs.get('enterprise')
    registration = attrs.get('registration')
    email = attrs.get('email')
    password = attrs.get('password')

    if not first_name:
        errors['first_name'] = ['O primeiro nome do usuário não pode ser vazio.']

    if not last_name:
        errors['last_name'] = ['O sobrenome do usuário não pode ser vazio.']

    if not enterprise:
        errors['enterprise'] = ['O funcionário precisa estar associado a uma empresa.']

    if not registration:
        errors['registration'] = ['A matrícula do funcionário precisa ser preenchida.']
    else: 
        if registration and User.objects.filter(registration=registration).exists():
            errors.setdefault('registration', []).append('Essa matricula já esta em uso')

    if not email:
        errors['email'] = ['O email não pode ser vazio.']
    else:
        if '@' not in email or '.com' not in email:
            errors.setdefault('email', []).append('Email inválido.')

    if not password:
        errors['password'] = ['Sua senha não pode ser vazia.']
    else:
        if len(password) < 8 or len(password) > 25:
            errors.setdefault('password', []).append('Sua senha deve ter entre 8 a 25 caracteres.')

        if not any(not c.isalnum() for c in password):
            errors.setdefault('password', []).append('Sua senha precisa conter pelo menos um caractere especial.')

    if errors:
        raise serializers.ValidationError(errors)

    return attrs