from core.models import Topic
from core.serializers import TopicSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from usuario.models import Usuario as User
from django_filters.rest_framework import DjangoFilterBackend
from filters import TopicFilter

class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TopicFilter

    def get_queryset(self):
        user = self.request.user    
        if user.is_authenticated and not user.is_superuser:
            user_data = User.objects.get(email=user)
            return Topic.objects.filter(enterprise_topic=user_data.enterprise)
        return Topic.objects.all()