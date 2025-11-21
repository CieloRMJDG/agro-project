from django.contrib import admin
from .models import Sensor, Lectura


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'activo', 'ubicacion')


@admin.register(Lectura)
class LecturaAdmin(admin.ModelAdmin):
	list_display = ('id', 'sensor', 'fecha_hora', 'temperatura', 'humedad', 'ph')
	list_filter = ('sensor',)
