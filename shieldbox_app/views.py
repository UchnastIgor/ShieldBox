from django.shortcuts import render
from django.http import JsonResponse
from .models import ShieldBox, TemperatureSensor, SmokeSensor
from .serializers import ShieldBoxSerializer, TemperatureSensorSerializer, SmokeSensorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, generics


# Create your views here.

@api_view(['GET', 'POST'])
def shieldbox_list(request, format = None):
    if request.method == 'GET':
        devices = ShieldBox.objects.all()
        serializer = ShieldBoxSerializer(devices, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ShieldBoxSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def shieldbox_id(request, device_id , format = None):
    if request.method == 'GET':
        device = ShieldBox.objects.get(id=device_id)
        serializer = ShieldBoxSerializer(device, many = False)
        return Response(serializer.data, status = status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ShieldBoxSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def shieldbox_temp_sensor(request, device_id, format = None):
    try:
        device = ShieldBox.objects.get(id=device_id)
    except ShieldBox.DoesNotExist:
        return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sensors = TemperatureSensor.objects.filter(device = device)
        serializer = TemperatureSensorSerializer(sensors, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = TemperatureSensor(data = request.data)
        if serializer.is_valid():
            serializer.save(device = device)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def shieldbox_smoke_sensor(request, device_id, format = None):
    try:
        device = ShieldBox.objects.get(id=device_id)
    except ShieldBox.DoesNotExist:
        return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sensors = SmokeSensor.objects.filter(device = device)
        serializer = SmokeSensorSerializer(sensors, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = SmokeSensor(data = request.data)
        if serializer.is_valid():
            serializer.save(device = device)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    