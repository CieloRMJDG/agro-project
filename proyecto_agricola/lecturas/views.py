from django.shortcuts import render

# Create your views here.
# lecturas/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Avg, Min, Max, Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Lectura, Sensor
from .serializers import LecturaSerializer, SensorSerializer
from .filters import LecturaFilter # Importamos el filtro

# ===================================================================
# A. ViewSet para CRUD (Lectura)
# ===================================================================
class LecturaViewSet(viewsets.ModelViewSet):
    """
    Provee las acciones CRUD para las Lecturas de Sensores.
    Los endpoints se generan automáticamente (POST, GET lista, GET detalle, PUT/PATCH, DELETE).
    """
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer
    
    # Configuración de Filtros y Ordenamiento
    filter_backends = [DjangoFilterBackend]
    filterset_class = LecturaFilter # Aplica los dos filtros obligatorios
    
    # 🎯 ENDPOINT ADICIONAL DE LÓGICA (Requisito del proyecto)
    @action(detail=False, methods=['get'])
    def resumen_por_sensor(self, request):
        """
        Calcula el promedio, máximo, mínimo y conteo de lecturas por cada sensor.
        Ruta: /api/lecturas/resumen_por_sensor/
        """
        resumen = Lectura.objects.values(
            'sensor__id',
            'sensor__nombre',
        ).annotate(
            promedio_temperatura=Avg('temperatura'),
            maximo_temperatura=Max('temperatura'),
            minimo_temperatura=Min('temperatura'),

            promedio_humedad=Avg('humedad'),
            maximo_humedad=Max('humedad'),
            minimo_humedad=Min('humedad'),

            promedio_ph=Avg('ph'),
            maximo_ph=Max('ph'),
            minimo_ph=Min('ph'),

            conteo=Count('id')
        ).order_by('sensor__nombre')

        return Response(resumen)

# ===================================================================
# B. ViewSet para CRUD (Sensor - si te corresponde esta app)
# ===================================================================
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Vista simple tipo "dashboard" que muestra sensores y últimas lecturas
from django.shortcuts import render


def dashboard_view(request):
    sensors = Sensor.objects.all().order_by('nombre')
    # Para cada sensor traemos las 5 lecturas más recientes
    sensor_data = []
    for s in sensors:
        recent = s.lecturas.order_by('-fecha_hora')[:5]
        sensor_data.append({'sensor': s, 'recent': recent})

    return render(request, 'lecturas/dashboard.html', {'sensor_data': sensor_data})