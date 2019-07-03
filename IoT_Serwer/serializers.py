from rest_framework.serializers import ModelSerializer
from .models import RGBDevice, OnOffDevice, ProgramDevice, PercentDevice, ErrorData, Sensor


class SerializerRGB(ModelSerializer):
    class Meta:
        model = RGBDevice
        fields = (
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
            'date',
            'red',
            'blue',
            'green'
        )


class SerializerOnOff(ModelSerializer):
    class Meta:
        model = OnOffDevice
        fields = (
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
            'date',
            'turnedON'
        )


class SerializerProgrammed(ModelSerializer):
    class Meta:
        model = ProgramDevice
        fields = (
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
            'date',
            'program'
        )


class SerializerPercent(ModelSerializer):
    class Meta:
        model = PercentDevice
        fields = (
            'name',
            'group',
            'room',
            'errorState',
            'date',
            'data'
        )

# Space for new types of Devices


class ErrorSerializer(ModelSerializer):
    class Meta:
        model = ErrorData
        fields = (
            'date',
            'code',
            'name',
            'group',
            'room',
        )


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = (
            'name',
            'group',
            'room',
            'errorState',
            'date',
            'data'
        )
