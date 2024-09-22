from django.urls import path
from .views import CreateSensorAPIView, ListUpdateAPIView, ListSensorAPIView, RetrieveSensorAPIView

urlpatterns = [
    path('sensors/', ListSensorAPIView.as_view()),
    #path('list/', ListSensorAPIView.as_view()),
    path('sensors/<int:pk>/', CreateSensorAPIView.as_view()),
    path('measurements/', ListUpdateAPIView.as_view()),
    path('sensors/<int:pk>', RetrieveSensorAPIView.as_view())
]


