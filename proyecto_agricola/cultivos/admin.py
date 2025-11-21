from django.contrib import admin
from .models import Cultivo, EtapaCultivo, Riego

@admin.register(Cultivo)
class CultivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'fecha_siembra')
    search_fields = ('nombre', 'tipo')
    list_filter = ('tipo', 'fecha_siembra')

@admin.register(EtapaCultivo)
class EtapaCultivoAdmin(admin.ModelAdmin):
    list_display = ('etapa', 'cultivo', 'fecha_inicio')
    search_fields = ('etapa', 'cultivo__nombre')
    list_filter = ('fecha_inicio', 'cultivo')

@admin.register(Riego)
class RiegoAdmin(admin.ModelAdmin):
    list_display = ('cultivo', 'fecha', 'cantidad_litros', 'frecuencia')
    search_fields = ('cultivo__nombre', 'frecuencia')
    list_filter = ('frecuencia', 'fecha', 'cultivo')
    date_hierarchy = 'fecha'
