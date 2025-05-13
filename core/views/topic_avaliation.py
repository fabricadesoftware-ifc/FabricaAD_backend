from core.models import TopicAvaliation
from core.serializers import TopicAvaliationSerializer
from rest_framework.viewsets import ModelViewSet

class TopicAvaliationViewSet(ModelViewSet):
    
    queryset = TopicAvaliation.objects.all()
    serializer_class = TopicAvaliationSerializer