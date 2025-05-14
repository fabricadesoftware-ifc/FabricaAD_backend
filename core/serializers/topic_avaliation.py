from core.models import TopicAvaliation
from rest_framework.serializers import ModelSerializer
from .topic import TopicSerializer

class TopicAvaliationSerializer(ModelSerializer):
    topic = TopicAvaliation()
    class Meta:
        model = TopicAvaliation
        fields = '__all__'
