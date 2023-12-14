from rest_framework import serializers
from .models import SensorsData
# import base64

class SensorsDataSerializer(serializers.ModelSerializer):
    shieldbox_name = serializers.StringRelatedField()
    sensors_data = serializers.FloatField()
    class Meta:
        model = SensorsData
        fields = ("id", "shieldbox_name", "sensors_data")