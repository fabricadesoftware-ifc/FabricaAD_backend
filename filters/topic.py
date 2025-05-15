import django_filters
from core.models import Topic

class TopicFilter(django_filters.FilterSet):
    topic_filter = django_filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = Topic
        fields = ['title','enterprise_topic']