import django_filters as filters
from core.models import Position

class PositionFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Position
        fields = ['name']