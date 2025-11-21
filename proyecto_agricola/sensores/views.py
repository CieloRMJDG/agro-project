from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import TipoSensor, Sensor
from .serializers import TipoSensorSerializer, SensorSerializer


class TipoSensorViewSet(viewsets.ModelViewSet):
    queryset = TipoSensor.objects.all()
    serializer_class = TipoSensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'ubicacion']
    ordering_fields = ['fecha_instalacion']

    @action(detail=False, methods=['get'])
    def activos(self, request):
        sensores_activos = Sensor.objects.filter(activo=True)
        serializer = self.get_serializer(sensores_activos, many=True)
        return Response({
            "total_activos": sensores_activos.count(),
            "sensores": serializer.data
        })
