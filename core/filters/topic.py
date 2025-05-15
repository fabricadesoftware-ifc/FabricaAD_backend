import djando_filters
from core.models import Topic

class TopicFilter(djando_filters.FilterSet):
    topic_filter = djando_filters.SlugRelatedField(lookup_expr="icontains")
    
    class Meta:
        model = Topic
        fields = ['title','enterprise_topic']