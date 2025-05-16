import django_filters as filters
from core.models import Sector

class SectorFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    enterprise = filters.CharFilter(field_name='enterprise__name', lookup_expr='icontains')

    class Meta:
        model = Sector
        fields = ['name', 'enterprise']