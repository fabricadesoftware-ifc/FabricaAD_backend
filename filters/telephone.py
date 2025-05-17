import django_filters
from core.models import Telephone

class TelephoneFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(field_name='number', lookup_expr='icontains')
    type = django_filters.CharFilter(field_name='type', lookup_expr='icontains')

    class Meta:
        model = Telephone
        fields = ['number', 'type']