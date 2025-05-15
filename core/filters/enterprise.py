import django_filters
from core.models import Enterprise

class EnterpriseFilter(django_filters.FilterSet):
    name = django_filters.Charfilter(lookup_expr="icontains")

    class Meta:
        model = Enterprise
        fields = ['nome']