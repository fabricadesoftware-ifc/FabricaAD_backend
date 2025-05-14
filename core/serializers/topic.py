from core.models import Topic, Enterprise
from rest_framework.serializers import ModelSerializer, SlugRelatedField

class TopicSerializer(ModelSerializer):
    enterprise_topic = SlugRelatedField(slug_field='name', queryset=Enterprise.objects.all())
    class Meta:
        model = Topic
        fields = '__all__'
        depth = 1