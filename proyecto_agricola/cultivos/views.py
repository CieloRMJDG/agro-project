from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cultivo, EtapaCultivo, Riego
from .serializers import CultivoSerializer, EtapaCultivoSerializer, RiegoSerializer
from django.db.models import Count

# ---- CRUD de Cultivo ----
class CultivoListCreate(generics.ListCreateAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer

    # filtros
    def get_queryset(self):
        queryset = super().get_queryset()
        tipo = self.request.query_params.get('tipo')
        fecha = self.request.query_params.get('fecha_siembra')

        if tipo:
            queryset = queryset.filter(tipo__icontains=tipo)
        if fecha:
            queryset = queryset.filter(fecha_siembra=fecha)

        return queryset


class CultivoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer


# ---- CRUD de EtapaCultivo ----
class EtapaListCreate(generics.ListCreateAPIView):
    queryset = EtapaCultivo.objects.all()
    serializer_class = EtapaCultivoSerializer


class EtapaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EtapaCultivo.objects.all()
    serializer_class = EtapaCultivoSerializer


# ---- CRUD de Riego ----
class RiegoListCreate(generics.ListCreateAPIView):
    queryset = Riego.objects.all()
    serializer_class = RiegoSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        cultivo_id = self.request.query_params.get('cultivo_id')
        frecuencia = self.request.query_params.get('frecuencia')
        
        if cultivo_id:
            queryset = queryset.filter(cultivo_id=cultivo_id)
        if frecuencia:
            queryset = queryset.filter(frecuencia=frecuencia)
        
        return queryset


class RiegoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Riego.objects.all()
    serializer_class = RiegoSerializer


# ---- Endpoint extra ----
@api_view(['GET'])
def resumen_cultivos(request):
    data = Cultivo.objects.values('tipo').annotate(total=Count('id'))
    return Response(data)
