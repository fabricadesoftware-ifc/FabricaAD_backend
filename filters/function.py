import django_filters as filters
from core.models import Function
from django.db.models import Q

class FunctionFilter(filters.FilterSet):
    search_subordinates = filters.CharFilter(method='search_filter_subordinates')

    class Meta:
        model = Function
        fields = []

    def search_filter_subordinates(self, qs, name, value):
        return qs.filter(
            Q(employer__first_name__icontains=value) |
            Q(employer__last_name__icontains=value) |
            Q(employer__email__icontains=value) |
            Q(employer__registration__icontains=value) |
            Q(sector__name__icontains=value)
        )