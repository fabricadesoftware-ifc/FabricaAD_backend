import django_filters as filters
from core.models import Function

class FunctionFilter(filters.FilterSet):
    supervisor = filters.CharFilter(field_name='supervisor__username', lookup_expr='icontains')
    employer = filters.CharFilter(field_name='employer__username', lookup_expr='icontains')
    position = filters.CharFilter(field_name='position__name', lookup_expr='icontains')
    initial_date = filters.DateFilter(field_name='initial_date', lookup_expr='exact')
    final_date = filters.DateFilter(field_name='final_date', lookup_expr='exact')
    sector = filters.CharFilter(field_name='sector__name', lookup_expr='icontains')

    class Meta:
        model = Function
        fields = ['supervisor', 'employer', 'position', 'initial_date', 'final_date', 'sector']
