from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoSensorViewSet, SensorViewSet  

router = DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'tipos-sensores', TipoSensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
