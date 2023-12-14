from django.db import models

# Create your models here.
class SensorsData(models.Model):
    shieldbox_name = models.CharField(max_length=500)
    sensors_data = models.FloatField()
    # sensors_data = 20
    # def __str__(self) -> float:
    #     return self.sensors_data