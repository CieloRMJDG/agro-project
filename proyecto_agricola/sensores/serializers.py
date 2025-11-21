from rest_framework import serializers
from .models import TipoSensor, Sensor
from datetime import date, timedelta


class TipoSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSensor
        fields = "__all__"


class SensorSerializer(serializers.ModelSerializer):
    # Aceptar explícitamente formato ISO y validar el campo
    fecha_instalacion = serializers.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Sensor
        fields = "__all__"

    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del sensor debe tener al menos 3 caracteres.")
        return value

    def validate_fecha_instalacion(self, value):
       
        max_allowed = date.today() + timedelta(days=3)
        if value > max_allowed:
            raise serializers.ValidationError("La fecha no puede ser superior a 3 días desde hoy.")

        
        if not (1 <= value.year <= 9999):
            raise serializers.ValidationError("Año inválido en la fecha (debe tener como máximo 4 dígitos).")

        return value