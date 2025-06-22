from rest_framework import serializers
from core.models import Telephone

def validate_telephone(attrs):
    erros = {}

    number = attrs.get('number')
    user_phone = attrs.get('user_phone')
    enterprise_phone = attrs.get('enterprise_phone')

    if not number:
        erros['number'] = ['O campo "number" não pode ser vazio.']
    else:
        number = number.strip()
        if Telephone.objects.filter(number=number).exists():
            erros.setdefault('number', []).append('Esse telefone já está cadastrado.')
        if not number.isdigit():
            erros.setdefault('number', []).append('Número invalido: Telefone do usuário deve conter apenas dígitos.')
        if len(number) != 9:
            erros.setdefault('number', []).append('Número invalido: Telefone do usuário deve ter conter apenas 9 dígitos.')
        
    if not user_phone:
        erros['user_phone'] = ['O campo "user phone" não pode ser vazio.']
    else:
        if Telephone.objects.filter(user_phone=user_phone).exists():
            erros.setdefault('user_phone', []).append('Esse telefone já está cadastrado para outro usuário.')

    if not enterprise_phone:
        erros['enterprise_phone'] = ['O campo "enterprise phone" não pode ser vazio.']
    else:
        if Telephone.objects.filter(enterprise_phone=enterprise_phone).exists():
            erros.setdefault('enterprise_phone', []).append('Esse telefone já está cadastrado para outra empresa.')

    if erros:
        raise serializers.ValidationError(erros)
    
    return attrs

