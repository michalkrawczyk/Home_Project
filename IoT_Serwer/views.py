from .serializers import *

from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class RoomListAPI(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = SerializerRoom
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'id',
        'name',
        'enabled',
    )



class DeviceRGBDetailsAPI(RetrieveUpdateAPIView):
    queryset = RGBDevice.objects.all()
    serializer_class = SerializerRGB


class DeviceAPIListRGB(ListAPIView):
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


class DeviceOnOffDetails(RetrieveUpdateAPIView):
    queryset = OnOffDevice.objects.all()
    serializer_class = SerializerOnOff


class DeviceAPIListOnOff(ListAPIView):
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


class DeviceProgramDetails(RetrieveUpdateAPIView):
    queryset = ProgramDevice.objects.all()
    serializer_class = SerializerProgrammed


class DeviceAPIListProgrammed(ListAPIView):
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


class DevicePercentDetails(RetrieveUpdateAPIView):
    queryset = PercentDevice.objects.all()
    serializer_class = SerializerPercent


class DeviceAPIListPercent(ListAPIView):
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
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = (
         'id',
         'name',
         'group',
         'room',
         'code'
    )
    ordering = ('-date',)


class SensorDetails(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorListAPIView(ListAPIView):
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
# TODO : Consider - Ordering by date
# TODO :HTML/CSS views ?
# TODO : Future: Permissions
