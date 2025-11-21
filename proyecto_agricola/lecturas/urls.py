# lecturas/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LecturaViewSet, SensorViewSet

router = DefaultRouter()
router.register(r'lecturas', LecturaViewSet)
router.register(r'sensores', SensorViewSet)

urlpatterns = [
    # Incluye las rutas del router (CRUD, filtros y el @action)
    path('', include(router.urls)),
]