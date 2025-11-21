from django.db import models

class TipoSensor(models.Model):
    nombre = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Sensor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoSensor, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=150, blank=True, null=True)
    fecha_instalacion = models.DateField()

    def __str__(self):
        return self.nombre
