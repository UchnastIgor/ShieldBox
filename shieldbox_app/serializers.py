from .models import TemperatureSensor, ShieldBox, SmokeSensor
from rest_framework import serializers

class TemperatureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureSensor
        # fields = ['temp_value', 'time']
        fields = ['temp_value']
        
class SmokeSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmokeSensor
        fields = ['smoke_value']

class ShieldBoxSerializer(serializers.ModelSerializer):
    temp_sensor = TemperatureSensorSerializer(many=True, read_only=False, source='temperaturesensor_set')
    smoke_sensor = SmokeSensorSerializer(many=True, read_only=False, source='smokesensor_set')

    class Meta:
        model = ShieldBox
        fields = ["id",'name','smoke_sensor', 'temp_sensor']