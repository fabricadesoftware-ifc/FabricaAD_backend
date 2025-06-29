from rest_framework.serializers import ValidationError
from datetime import datetime

def validate_avaliation(attrs):
    errors = {}
    
    strengths = attrs.get('strengths')
    weaknesses = attrs.get('weaknesses')
    next_evaluation_date = attrs.get('next_evaluation_date')

    if not strengths:
        errors['strengths'] = ['preencha os pontos fortes do avaliado']

    if not weaknesses:
        errors['weaknesses'] = ['preencha os pontos fracos do avaliado']

    if not next_evaluation_date:
        errors['next_evaluation_date'] = ['preencha a proxima data de avaliação']
    else:
        if next_evaluation_date <= datetime.now().date():
            errors.setdefault('next_evaluation_date', []).append('a data da proxima avaliação não pode ser menor que a data de hoje')

    
    if errors:
        raise ValidationError(errors)
    
    
    return attrs