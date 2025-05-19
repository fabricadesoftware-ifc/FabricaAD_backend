import django_filters
from usuario.models import Usuario as User

class EmployerFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
    registration = django_filters.CharFilter(field_name='registration', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['email', 'registration', 'name']
