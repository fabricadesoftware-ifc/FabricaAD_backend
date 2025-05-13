from core.models import TopicAvaliation
from rest_framework.serializers import ModelSerializer

class TopicAvaliationSerializer(ModelSerializer):
    class Meta:
        model = TopicAvaliation
        fields = '__all__'
        depth = 1
