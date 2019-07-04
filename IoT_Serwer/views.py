from .serializers import *

from rest_framework.generics import (
    RetrieveDestroyAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    ListAPIView
)
from django_filters.rest_framework import DjangoFilterBackend


class DeviceRGBDetailsAPI(RetrieveUpdateDestroyAPIView):
    queryset = RGBDevice.objects.all()
    serializer_class = SerializerRGB


class DeviceAPIListRGB(ListCreateAPIView):
    queryset = RGBDevice.objects.all()
    serializer_class = SerializerListRGB
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'name',
        'group',
        'room',
        'manualControl',
        'errorState',
    )


# End of RGB Devices


class DeviceOnOffDetails(RetrieveUpdateDestroyAPIView):
    queryset = OnOffDevice.objects.all()
    serializer_class = SerializerOnOff


class DeviceAPIListOnOff(ListCreateAPIView):
    queryset = OnOffDevice.objects.all()
    serializer_class = SerializerOnOff
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'name',
        'group',
        'room',
        'manualControl',
        'errorState',
        'turnedON'
    )

# End of On/Off Devices


class DeviceProgramDetails(RetrieveUpdateDestroyAPIView):
    queryset = ProgramDevice.objects.all()
    serializer_class = SerializerProgrammed

# End of Programmed Devices


class DevicePercentDetails(RetrieveUpdateDestroyAPIView):
    queryset = PercentDevice.objects.all()
    serializer_class = SerializerPercent

# End of Percent determined Devices


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
# TODO : Device by rooms,group,Manual Control, Error State - requires new serializers + turnedOn for OnOff
# TODO : Sensors by rooms,group,Error State - requires new serializers
# TODO : Consider - Ordering by date
# TODO :HTML views ?

