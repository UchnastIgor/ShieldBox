from django.shortcuts import render
from django.http import JsonResponse
from .models import ShieldBox, TemperatureSensor
from .serializers import ShieldBoxSerializer, TemperatureSensorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, generics


# Create your views here.
# @api_view(['GET', 'POST'])
# def currentview(request):
#     sensordata = TemperatureSensor.objects.all()
#     context = {
#         "name": sensordata.name,
#         'value': sensordata.value,
#     }
    
#     return JsonResponse({"name": sensordata.name, 'value': sensordata.value})

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
def shieldbox_sensors(request, device_id, format = None):
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

@api_view(['GET', 'PUT', 'DELETE'])
def shieldbox_sensor_detail(request, device_id, name, format = None):
    try:
        device = ShieldBox.objects.get(id = device_id)
    except ShieldBox.DoesNotExist:
        return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        sensor = TemperatureSensor.objects.get(device = device, name = name)
    except TemperatureSensor.DoesNotExist:
         return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TemperatureSensorSerializer(sensor)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = TemperatureSensorSerializer(sensor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        serializer = TemperatureSensorSerializer(sensor)
        sensor.delete()
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
    