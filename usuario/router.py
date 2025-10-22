from rest_framework.routers import DefaultRouter

from usuario import views

app_name = "usuario"

router = DefaultRouter()
router.register("users", views.UsuarioViewSet, basename='users')
