# lecturas/models.py
from django.db import models

class Sensor(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='lecturas')
    fecha_hora = models.DateTimeField()
    temperatura = models.FloatField()
    humedad = models.FloatField()
    ph = models.FloatField()

    def __str__(self):
        return f"{self.sensor.nombre} - {self.fecha_hora}"
