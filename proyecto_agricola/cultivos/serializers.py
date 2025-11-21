from rest_framework import serializers
from .models import Cultivo, EtapaCultivo, Riego
from datetime import date

class EtapaCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtapaCultivo
        fields = '__all__'


class RiegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riego
        fields = '__all__'
    
    def validate_cantidad_litros(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad de litros debe ser mayor a 0.")
        return value


class CultivoSerializer(serializers.ModelSerializer):
    etapas = EtapaCultivoSerializer(many=True, read_only=True)
    riegos = RiegoSerializer(many=True, read_only=True)

    class Meta:
        model = Cultivo
        fields = '__all__'

    # Validaciones
    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener mínimo 3 caracteres.")
        return value

    def validate_fecha_siembra(self, value):
        if value > date.today():
            raise serializers.ValidationError("La fecha de siembra no puede ser futura.")
        return value
