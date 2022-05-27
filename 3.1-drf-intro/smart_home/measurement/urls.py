from django.urls import path

from measurement.views import ListCreateSensors, CreateMeasurement, RetrieveUpdateSensor

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ListCreateSensors.as_view()),
    path('measurement/', CreateMeasurement.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensor.as_view())
]
