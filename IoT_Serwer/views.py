from .serializers import *

from rest_framework.generics import (
    RetrieveDestroyAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
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
    serializer_class = SerializerListOnOff
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


class DeviceAPIListProgrammed(ListCreateAPIView):
    queryset = ProgramDevice.objects.all()
    serializer_class = SerializerListProgrammed
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'name',
        'group',
        'room',
        'manualControl',
        'errorState',
    )
# End of Programmed Devices


class DevicePercentDetails(RetrieveUpdateDestroyAPIView):
    queryset = PercentDevice.objects.all()
    serializer_class = SerializerPercent


class DeviceAPIListPercent(ListCreateAPIView):
    queryset = PercentDevice.objects.all()
    serializer_class = SerializerListPercent
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'name',
        'group',
        'room',
        'manualControl',
        'errorState',
    )
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


class SensorListAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SerializerSensorList
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'name',
        'group',
        'room',
        'errorState',
    )

# TODO: Rename Views for clarity in urls
# TODO : Sensors by rooms,group,Error State - requires new serializers
# TODO : Consider - Ordering by date
# TODO : Consider - Delete ErrorDataDetails and expand ErrorDataListAPIView by filter 'id'
# TODO :HTML/CSS views ?
# TODO :Permissions

