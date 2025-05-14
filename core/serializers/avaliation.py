from core.models import Avaliation, TopicAvaliation
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from usuario.models import Usuario as User
from usuario.serializers import UsuarioInfoAvaliationSerializer
from .topic_avaliation import TopicAvaliationSerializer

class AvaliationSerializer(ModelSerializer):
    evaluated = UsuarioInfoAvaliationSerializer()
    evaluator = UsuarioInfoAvaliationSerializer()
    class Meta:
        model = Avaliation
        fields = '__all__'
        depth = 1

class AvaliationCreateSerializer(ModelSerializer):
    evaluated = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    evaluator = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    topics = TopicAvaliationSerializer(many=True, required=False)
    
    class Meta:
        model = Avaliation
        fields = '__all__'

    def create(self, validate_data):
       topics_obj = validate_data.pop("topics", [])

       avaliation = super().create(validate_data)

       for topic in topics_obj:
            TopicAvaliation.objects.create(avaliation=avaliation, **topic)

       topics_created = TopicAvaliation.objects.filter(avaliation=avaliation).all()

       total = sum(topic.score for topic in topics_created) / len(topics_created) 
        
       avaliation_created = Avaliation.objects.get(pk=avaliation.id)

       avaliation_created.score = total

       avaliation_created.save()

       return avaliation_created