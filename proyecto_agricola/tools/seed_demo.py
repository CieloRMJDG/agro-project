import os
import django
from django.utils import timezone
from random import uniform, randint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_agricola.settings')
django.setup()

from lecturas.models import Sensor, Lectura

# Crear dos sensores
s1, created = Sensor.objects.get_or_create(nombre='Sensor A', defaults={'activo': True, 'ubicacion': 'Parcela 1'})
s2, created = Sensor.objects.get_or_create(nombre='Sensor B', defaults={'activo': True, 'ubicacion': 'Parcela 2'})

# Crear lecturas recientes para ambos
now = timezone.now()
for i in range(10):
    Lectura.objects.create(
        sensor=s1,
        fecha_hora=now - timezone.timedelta(hours=i),
        temperatura=round(uniform(15.0, 30.0), 2),
        humedad=round(uniform(30.0, 80.0), 2),
        ph=round(uniform(5.5, 7.5), 2),
    )

for i in range(8):
    Lectura.objects.create(
        sensor=s2,
        fecha_hora=now - timezone.timedelta(hours=i*2),
        temperatura=round(uniform(10.0, 28.0), 2),
        humedad=round(uniform(35.0, 70.0), 2),
        ph=round(uniform(6.0, 8.0), 2),
    )

print('Seed complete: sensors and readings created.')
