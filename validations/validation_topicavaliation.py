from rest_framework.serializers import ValidationError
from core.models import TopicAvaliation

def validate_topicavaliation(attrs):
    errors = {}

    topic = attrs.get('topic')
    score = attrs.get('score')
    feedback = attrs.get('feedback')

    if not topic:
        errors['topic'] = ['O tópico não pode ser vazio.']

    if not score:
        errors['score'] = ['A pontuação não pode ser vazia.']

    if not feedback:
        errors['feedback'] = ['O feedback não pode ser vazio.']
    
    if errors:
        raise ValidationError(errors)
    
    return attrs