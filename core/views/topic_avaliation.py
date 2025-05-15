from core.models import TopicAvaliation
from core.serializers import TopicAvaliationSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TopicAvaliationViewSet(ModelViewSet):
    queryset = TopicAvaliation.objects.all()
    serializer_class = TopicAvaliationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


