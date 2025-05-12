from core.models import Topic
from rest_framework.serializers import ModelSerializer

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        depth = 1