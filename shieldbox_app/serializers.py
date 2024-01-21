from .models import TemperatureSensor, ShieldBox, SmokeSensor
from rest_framework import serializers

class TemperatureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureSensor
        fields = ['temp_value', 'time']
        
class SmokeSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmokeSensor
        fields = ['smoke_value']

class ShieldBoxSerializer(serializers.ModelSerializer):
    temp_sensor = TemperatureSensorSerializer(many=True, read_only=True, source='temperaturesensor_set')
    smoke_sensor = SmokeSensorSerializer(many=True, read_only=True, source='smokesensor_set')

    class Meta:
        model = ShieldBox
        fields = ['name','smoke_sensor', 'temp_sensor']