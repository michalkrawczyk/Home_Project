from rest_framework import serializers

from .models import RGBDevice, OnOffDevice, ProgramDevice, PercentDevice, ErrorData, Sensor

# Todo: Test with views


class SerializerRGB(serializers.ModelSerializer):
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


class SerializerOnOff(serializers.ModelSerializer):
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


class SerializerProgrammed(serializers.ModelSerializer):
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


class SerializerPercent(serializers.ModelSerializer):
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


class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorData
        fields = (
            'date',
            'code',
            'name',
            'group',
            'room',
        )


class SensorSerializer(serializers.ModelSerializer):
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
