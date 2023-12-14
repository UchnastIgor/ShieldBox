from django.shortcuts import render
from rest_framework import generics
from .models import SensorsData
from .serializers import SensorsDataSerializer

# Create your views here.
class SensorsDataView(generics.ListAPIView):
    queryset = SensorsData.objects.all()
    serializer_class = SensorsDataSerializer