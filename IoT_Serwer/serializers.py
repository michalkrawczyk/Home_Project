from rest_framework import serializers

from .models import RGBDevice, OnOffDevice , FixedDevice , ProgramDevice

# Todo: Test with views
# Todo: Check for smoother way


class SerializerRGB(serializers.ModelSerializer):
    class Meta:
        model = RGBDevice
        fields = (
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
            # 'date',
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
            # 'date',
            'turnedON'
        )


class SerializerFixed(serializers.ModelSerializer):
    class Meta:
        model = FixedDevice
        fields = (
            'name',
            'group',
            'room',
            'manualControl',
            'errorState',
            # 'date',
            'data'
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
            # 'date',
            'program'
        )
