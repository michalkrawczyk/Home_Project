from .serializers import *

from rest_framework.generics import (
    RetrieveDestroyAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from django_filters.rest_framework import DjangoFilterBackend


class DeviceRGBDetails(RetrieveUpdateDestroyAPIView):
    queryset = RGBDevice.objects.all()
    serializer_class = SerializerRGB


class DeviceOnOffDetails(RetrieveUpdateDestroyAPIView):
    queryset = OnOffDevice.objects.all()
    serializer_class = SerializerOnOff


class DeviceProgramDetails(RetrieveUpdateDestroyAPIView):
    queryset = ProgramDevice.objects.all()
    serializer_class = SerializerProgrammed


class DevicePercentDetails(RetrieveUpdateDestroyAPIView):
    queryset = PercentDevice.objects.all()
    serializer_class = SerializerPercent


# Space for new types of Device
class ErrorDataListAPIView(ListCreateAPIView):
    queryset = ErrorData.objects.all()
    serializer_class = ErrorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'code',
        'name',
        'group',
        'room',
    )


class ErrorDataDetails(RetrieveAPIView):
    queryset = ErrorData.objects.all()
    serializer_class = ErrorSerializer


class SensorDetails(RetrieveDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer



# TODO: Consider post vs put for Devices (now - put)
# TODO: Rename Views for clarity in urls
# TODO :HTML views ?

