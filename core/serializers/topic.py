from core.models import Topic, Enterprise
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from validations import validate_topic

class TopicSerializer(ModelSerializer):
    enterprise_topic = SlugRelatedField(slug_field='name', queryset=Enterprise.objects.all())
    class Meta:
        model = Topic
        fields = '__all__'
        depth = 1

    def validate(self, attrs):
        return validate_topic(attrs)
    