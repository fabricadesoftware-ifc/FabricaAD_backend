from core.models import Topic
from core.serializers import TopicSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from usuario.models import Usuario as User

class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        user_data = User.objects.get(email=user)    
        if user.is_authenticated and not user.is_superuser:
            return Topic.objects.filter(enterprise_topic=user_data.enterprise)
        return Topic.objects.all()