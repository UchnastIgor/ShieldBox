from django.contrib import admin
from .models import TemperatureSensor, ShieldBox, SmokeSensor
# Register your models here.
admin.site.register(ShieldBox)
admin.site.register(TemperatureSensor)
admin.site.register(SmokeSensor)
