from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import (
    Room,
    RGBDevice, OnOffDevice, ProgramDevice, PercentDevice, ErrorData, Sensor
)


class SerializerRoom(ModelSerializer):
    id = ReadOnlyField()

    class Meta:
        model = Room
        fields = (
            'id',
            'name',
            'enabled'
        )
# End of Rooms


class SerializerRGB(ModelSerializer):
    class Meta:
        model = RGBDevice
        fields = (
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
            'lastChange',
            'red',
            'blue',
            'green'
        )


class SerializerListRGB(ModelSerializer):
    id = ReadOnlyField()

    class Meta:
        model = RGBDevice
        fields = (
            'id',
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
        )

# End of RGB Devices


class SerializerOnOff(ModelSerializer):
    class Meta:
        model = OnOffDevice
        fields = (
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
            'lastChange',
            'turnedON'
        )


class SerializerListOnOff(ModelSerializer):
    id = ReadOnlyField()

    class Meta:
        model = OnOffDevice
        fields = (
            'id',
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
            'turnedON'
        )

# End of On/Off Devices


class SerializerProgrammed(ModelSerializer):
    class Meta:
        model = ProgramDevice
        fields = (
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
            'lastChange',
            'program'
        )


class SerializerListProgrammed(ModelSerializer):
    id = ReadOnlyField()

    class Meta:
        model = ProgramDevice
        fields = (
            'id',
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
        )

# End of Programmed Devices


class SerializerPercent(ModelSerializer):
    class Meta:
        model = PercentDevice
        fields = (
            'name',
            'group',
            'room',
            'errorState',
            'lastChange',
            'data'
        )


class SerializerListPercent(ModelSerializer):
    id = ReadOnlyField()

    class Meta:
        model = PercentDevice
        fields = (
            'id',
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
        )

# End of Percent determined Devices
# Space for new types of Devices


class ErrorSerializer(ModelSerializer):
    id = ReadOnlyField()

    class Meta:
        model = ErrorData
        fields = (
            'id',
            'date',
            'code',
            'name',
            'group',
            'room',
        )

# End of ErrorData Serializers


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = (
            'name',
            'group',
            'room',
            'errorState',
            'lastChange',
            'data'
        )


class SerializerSensorList(ModelSerializer):
    id = ReadOnlyField()

    class Meta:
        model = PercentDevice
        fields = (
            'id',
            'name',
            'group',
            'room',
            'errorState',
            'lastChange',
        )
# End of Sensor Serializers
