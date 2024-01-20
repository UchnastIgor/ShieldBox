from django.urls import path, include
from shieldbox_app import views

urlpatterns = [
    path('', views.shieldbox_list),
    path('shieldbox/<int:device_id>/', views.shieldbox_id),
    path('shieldbox/<int:device_id>/temp/', views.shieldbox_temp_sensor),
    path('shieldbox/<int:device_id>/smoke/', views.shieldbox_smoke_sensor),
    # path('<int:device_id>/sensors/<str:name>', views.shieldbox_sensor_detail),
]