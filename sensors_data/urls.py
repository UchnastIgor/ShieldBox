from django.urls import path, include
from .views import SensorsDataView

urlpatterns = [
    path('sensorslist/', SensorsDataView.as_view(),),
]