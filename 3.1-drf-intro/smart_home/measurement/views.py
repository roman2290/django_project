# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


# from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorListSerializer, SensorDetailSerializer, MeasurementSerializer
#from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView




class ListSensorAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer

    def post(self, request):
        review = SensorDetailSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response({'ststus': 'ok'})

#Получение датчиков
# class ListSensorAPIView(ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorListSerializer


# #Создать датчик
# class SensorCreateAPIView(ListCreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer

#     def post(self, request):
#         review = SensorDetailSerializer(data=request.data)
#         if review.is_valid():
#             review.save()
#         return Response({'status': 'OK'})

#Обновить датчик
class CreateSensorAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sen_sor = Sensor.objects.get(pk=pk)
        seri_alizer = SensorDetailSerializer(sen_sor, data = request.data)
        if seri_alizer.is_valid():
            seri_alizer.save()
        return Response(seri_alizer.data)


#Добавить измерение
class ListUpdateAPIView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        review = MeasurementSerializer(data = request.data)
        if review.is_valid():
            review.save()
        return Response(review.data)

#получение информации по датчику
class RetrieveSensorAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer

    def get(self, request):
        review = SensorListSerializer(data = request.data)
        if review.is_valid():
            review.save()
        return Response(review.data)











