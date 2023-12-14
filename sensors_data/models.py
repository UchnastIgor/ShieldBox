from django.db import models

# Create your models here.
class SensorsData(models.Model):
    shieldbox_name = models.CharField(max_length=500)
    sensors_data = models.FloatField()
    def __str__(self) -> float:
        return self.sensors_data