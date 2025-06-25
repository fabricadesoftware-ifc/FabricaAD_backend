from core.models import TopicAvaliation
from rest_framework.serializers import ModelSerializer
from .topic import TopicSerializer
from validations import validate_topicavaliation

class TopicAvaliationSerializer(ModelSerializer):
    topic = TopicAvaliation()
    class Meta:
        model = TopicAvaliation
        fields = '__all__'

    def validate(self, attrs):
        return validate_topicavaliation(attrs)
    
    
