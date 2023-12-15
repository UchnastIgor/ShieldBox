from django.urls import path, include
from shieldbox_app import views

urlpatterns = [
    path('devices/', views.shieldbox_list),
    path('devices/<int:device_id>/sensors/', views.shieldbox_sensors),
    path('devices/<int:device_id>/sensors/<str:name>', views.shieldbox_sensor_detail),
    # path('devices/current', views.currentview),
]