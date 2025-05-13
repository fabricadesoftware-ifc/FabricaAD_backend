from core.models import Topic
from core.serializers import TopicSerializer
from rest_framework.viewsets import ModelViewSet

class TopicViewSet(ModelViewSet):
    
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer