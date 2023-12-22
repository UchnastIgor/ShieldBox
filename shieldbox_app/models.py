from django.db import models

# Create your models here.

class ShieldBox(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TemperatureSensor(models.Model):
    device = models.ForeignKey(ShieldBox, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    value = models.FloatField(max_length = 50)
    smoke_value = models.FloatField(max_length = 50)

    class Meta:
        unique_together = ('name', 'device', "smoke_value")

    def __str__(self):
        return self.name + ' ' + self.device.name
    