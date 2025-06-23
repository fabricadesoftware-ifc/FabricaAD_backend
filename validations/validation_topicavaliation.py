from rest_framework.serializers import ValidationError
from core.models import TopicAvaliation

def validate_topicavaliation(attrs):
    errors = {}

    topic = attrs.get('topic')
    avaliation = attrs.get('avaliation')
    score = attrs.get('score')
    feedback = attrs.get('feedback')

    if not topic:
        errors['topic'] = ['O tópico não pode ser vazio.']

    if not avaliation:
        errors['avaliation'] = ['A avaliação não pode ser vazia.']

    if not score:
        errors['score'] = ['A pontuação não pode ser vazia.']

    if not feedback:
        errors['feedback'] = ['O feedback não pode ser vazio.']
    
    if errors:
        raise ValidationError(errors)
    
    return attrs