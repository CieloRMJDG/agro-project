# lecturas/serializers.py
from rest_framework import serializers
from .models import Lectura, Sensor

# Serializer para el modelo Sensor
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class LecturaSerializer(serializers.ModelSerializer):
    # Mostrar nombre del sensor en la representación
    sensor_nombre = serializers.CharField(source='sensor.nombre', read_only=True)

    class Meta:
        model = Lectura
        fields = ['id', 'sensor', 'sensor_nombre', 'fecha_hora', 'temperatura', 'humedad', 'ph']
        read_only_fields = ('sensor_nombre',)

    # Validaciones sencillas: asegurarse que los valores numéricos existan
    def validate(self, data):
        # Por ahora validaciones simples; extender según sea necesario
        return data

    def validate_temperatura(self, value):
        # Temperatura plausible en Celsius
        if value is None:
            return value
        if value < -50 or value > 100:
            raise serializers.ValidationError("La temperatura debe estar en el rango -50..100 °C")
        return value

    def validate_humedad(self, value):
        if value is None:
            return value
        if value < 0 or value > 100:
            raise serializers.ValidationError("La humedad debe estar en el rango 0..100 %")
        return value

    def validate_ph(self, value):
        if value is None:
            return value
        if value < 0 or value > 14:
            raise serializers.ValidationError("El pH debe estar en el rango 0..14")
        return value

    def validate(self, data):
        # Validación a nivel de objeto: fecha no futura y sensor activo
        from django.utils import timezone

        fecha = data.get('fecha_hora')
        sensor = data.get('sensor')

        if fecha:
            now = timezone.now()
            if fecha > now:
                raise serializers.ValidationError({'fecha_hora': 'La fecha/hora no puede ser futura.'})

        if sensor and not getattr(sensor, 'activo', True):
            raise serializers.ValidationError({'sensor': 'El sensor seleccionado está inactivo.'})

        return data