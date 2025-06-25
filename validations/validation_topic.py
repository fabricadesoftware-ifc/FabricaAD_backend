from rest_framework.serializers import ValidationError
from core.models import Topic

def validate_topic(attrs):
    errors = {}
    
    title = attrs.get('title')
    enterprise_topic = attrs.get('enterprise_topic')

    if not title:
        errors['title'] = ['O título não pode ser vazio.']
    elif len(title) > 45:
        errors['title'] = ['O título não pode ter mais de 45 caracteres.']

    if not enterprise_topic:
        errors['enterprise_topic'] = ['O tópico precisa estar associado a uma empresa.']
    elif not isinstance(enterprise_topic, int):
        errors['enterprise_topic'] = ['O tópico precisa estar associado a uma empresa válida.']

    if errors:
        raise ValidationError(errors)
    
    return attrs