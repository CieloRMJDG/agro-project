import django_filters
from .models import Lectura


class LecturaFilter(django_filters.FilterSet):
    # Filtro por sensor (por id)
    sensor = django_filters.NumberFilter(field_name='sensor__id')

    # Filtro de rango de fechas usando el campo 'fecha_hora'
    fecha_inicio = django_filters.DateTimeFilter(
        field_name='fecha_hora', lookup_expr='gte', label='Fecha/hora inicio (>=)')

    fecha_fin = django_filters.DateTimeFilter(
        field_name='fecha_hora', lookup_expr='lte', label='Fecha/hora fin (<=)')

    # Rango de temperatura
    temperatura_min = django_filters.NumberFilter(field_name='temperatura', lookup_expr='gte')
    temperatura_max = django_filters.NumberFilter(field_name='temperatura', lookup_expr='lte')

    # Rango de humedad
    humedad_min = django_filters.NumberFilter(field_name='humedad', lookup_expr='gte')
    humedad_max = django_filters.NumberFilter(field_name='humedad', lookup_expr='lte')

    # Rango de pH
    ph_min = django_filters.NumberFilter(field_name='ph', lookup_expr='gte')
    ph_max = django_filters.NumberFilter(field_name='ph', lookup_expr='lte')

    class Meta:
        model = Lectura
        fields = [
            'sensor', 'fecha_inicio', 'fecha_fin',
            'temperatura_min', 'temperatura_max',
            'humedad_min', 'humedad_max',
            'ph_min', 'ph_max'
        ]