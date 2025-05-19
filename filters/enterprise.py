import django_filters
from core.models import Enterprise

class EnterpriseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Enterprise
        fields = ['name']