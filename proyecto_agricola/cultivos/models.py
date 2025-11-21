# Create your models here.
from django.db import models

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    fecha_siembra = models.DateField()

    def __str__(self):
        return self.nombre


class EtapaCultivo(models.Model):
    etapa = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    
    cultivo = models.ForeignKey(Cultivo, related_name="etapas", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.etapa} - {self.cultivo.nombre}"


class Riego(models.Model):
    FRECUENCIA_CHOICES = [
        ('diario', 'Diario'),
        ('interdiario', 'Interdiario'),
        ('semanal', 'Semanal'),
        ('quincenal', 'Quincenal'),
    ]
    
    cultivo = models.ForeignKey(Cultivo, related_name="riegos", on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad_litros = models.FloatField()
    frecuencia = models.CharField(max_length=20, choices=FRECUENCIA_CHOICES)
    notas = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Riego - {self.cultivo.nombre} ({self.fecha})"
