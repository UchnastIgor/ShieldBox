from django.urls import path, include
from shieldbox_app import views

urlpatterns = [
    path('', views.shieldbox_list),
    path('<int:device_id>/sensors/', views.shieldbox_sensors),
    path('<int:device_id>/sensors/<str:name>', views.shieldbox_sensor_detail),
    # path('devices/current', views.currentview),
]