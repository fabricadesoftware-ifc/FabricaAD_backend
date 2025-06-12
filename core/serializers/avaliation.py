from core.models import Avaliation, TopicAvaliation
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from usuario.models import Usuario as User
from usuario.serializers import UsuarioInfoSerializer
from .topic_avaliation import TopicAvaliationSerializer

class AvaliationSerializer(ModelSerializer):
    evaluated = UsuarioInfoSerializer()
    evaluator = UsuarioInfoSerializer()

    class Meta:
        model = Avaliation
        fields = '__all__'
        depth = 1

class AvaliationCreateSerializer(ModelSerializer):
    evaluated = SlugRelatedField(
        slug_field='registration',
        queryset=User.objects.all(),
        write_only=True
    )
    evaluator = SlugRelatedField(
        slug_field='registration',
        queryset=User.objects.all(),
        write_only=True
    )
    topics = TopicAvaliationSerializer(many=True, required=False, write_only=True)

    class Meta:
        model = Avaliation
        fields = '__all__'

    def create(self, validated_data):
        topics_obj = validated_data.pop("topics", [])

        avaliation = super().create(validated_data)

        for topic_data in topics_obj:
            TopicAvaliation.objects.create(avaliation=avaliation, **topic_data)

        topics_created = TopicAvaliation.objects.filter(avaliation=avaliation).all()

        if topics_created:
            total = sum(topic.score for topic in topics_created) / len(topics_created)
            avaliation.score = total
            avaliation.save()

        return avaliation
