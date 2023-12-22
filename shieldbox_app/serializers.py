from .models import TemperatureSensor, ShieldBox
from rest_framework import serializers

class TemperatureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureSensor
        fields = ['name', 'value', "smoke_value"]

class ShieldBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShieldBox
        fields = ['id', 'name']