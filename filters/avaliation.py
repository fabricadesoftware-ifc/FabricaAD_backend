import django_filters
from core.models import Avaliation

class AvaliationFilter(django_filters.FilterSet):
    date = django_filters.DateFilter()
    next_date = django_filters.DateFilter()
    evaluator = django_filters.CharFilter()
    evaluated = django_filters.CharFilter('')
    score = django_filters.NumberFilter(field_name='score')

    class Meta:
        model = Avaliation
        fields = ["evaluator__first_name", "evaluator__email", "evaluator__registration", "evaluated__first_name", "evaluated__registration", "evaluated__email", "score", "date", "next_date"] 