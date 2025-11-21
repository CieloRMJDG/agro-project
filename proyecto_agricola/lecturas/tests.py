from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Sensor, Lectura
from django.utils import timezone
from datetime import timedelta


class LecturasBasicTests(TestCase):
	def setUp(self):
		self.client = APIClient()
		# Crear sensor y una lectura de ejemplo
		self.sensor = Sensor.objects.create(nombre='SensorTest', activo=True)
		self.lectura = Lectura.objects.create(
			sensor=self.sensor,
			fecha_hora=timezone.now(),
			temperatura=20.5,
			humedad=55.0,
			ph=6.5,
		)

	def test_root_returns_200(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)
		self.assertIn('Servidor de la API Agrícola', resp.content.decode('utf-8'))

	def test_lecturas_list(self):
		resp = self.client.get('/api/lecturas/')
		self.assertEqual(resp.status_code, 200)
		# debe contener al menos una lectura
		data = resp.json()
		self.assertTrue(isinstance(data, list))
		self.assertGreaterEqual(len(data), 1)

	def test_ph_filter(self):
		# Añadir otra lectura con ph distinto
		Lectura.objects.create(
			sensor=self.sensor,
			fecha_hora=timezone.now(),
			temperatura=18.0,
			humedad=50.0,
			ph=7.8,
		)
		# Filtrar por ph range que incluya sólo la segunda lectura
		resp = self.client.get('/api/lecturas/?ph_min=7.0&ph_max=8.0')
		self.assertEqual(resp.status_code, 200)
		data = resp.json()
		# Debe contener al menos una lectura con ph 7.8
		self.assertTrue(any(abs(item.get('ph', 0) - 7.8) < 0.001 for item in data))

	def test_invalid_ph_validation(self):
		# Intentar crear lectura con ph inválido (>14)
		payload = {
			'sensor': self.sensor.id,
			'fecha_hora': (timezone.now()).isoformat(),
			'temperatura': 20.0,
			'humedad': 40.0,
			'ph': 20.0,
		}
		resp = self.client.post('/api/lecturas/', payload, format='json')
		self.assertEqual(resp.status_code, 400)
		self.assertIn('ph', resp.json())

	def test_fecha_futura_validation(self):
		future = timezone.now() + timedelta(days=2)
		payload = {
			'sensor': self.sensor.id,
			'fecha_hora': future.isoformat(),
			'temperatura': 20.0,
			'humedad': 40.0,
			'ph': 6.5,
		}
		resp = self.client.post('/api/lecturas/', payload, format='json')
		self.assertEqual(resp.status_code, 400)
		self.assertIn('fecha_hora', resp.json())
