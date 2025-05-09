from rest_framework.routers import DefaultRouter
from core import views
router = DefaultRouter()

router.register(r'functions', views.FunctionViewSet)
router.register(r'positions', views.PositionViewSet)


router.register(r'sectors', views.SectorViewSet)