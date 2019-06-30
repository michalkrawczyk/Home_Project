from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomModels:

    @staticmethod
    def percentage_field():
        return models.IntegerField(
            default=0,
            validators=[
                MinValueValidator(0),
                MaxValueValidator(100)
            ]
        )

    @staticmethod
    def color_field():
        return models.IntegerField(
            default=0,
            validators=[
                MinValueValidator(0),
                MaxValueValidator(255)
            ]
        )

    @staticmethod
    def group_field():
        return models.IntegerField(
            default=0,
            validators=[
                MinValueValidator(0),
                MaxValueValidator(127)
            ]
        )


class Device(models.Model):
    name = models.TextField(max_length=100)
    group = CustomModels.group_field()
    room = models.PositiveSmallIntegerField()
    manualControl = models.BooleanField(default=False)
    errorState = models.BooleanField(default=False)
    # date = models.DateTimeField()

    class Meta:
        abstract = True


class RGBDevice(Device):
    red = CustomModels.color_field()
    blue = CustomModels.color_field()
    green = CustomModels.color_field()


class OnOffDevice(Device):
    turnedON = models.BooleanField(default=False)


class FixedDevice(Device):
    data = models.DecimalField(max_digits=10, decimal_places=4)  # max 999999.9999


class ProgramDevice(Device):  # for devices with specified programs
    program = models.PositiveSmallIntegerField()


# Space for new types of Devices


class ErrorData(models.Model):
    date = models.DateTimeField()
    # below - needs to consider
    code = models.SmallIntegerField()               # or Enum,Text - now
    name = models.TextField(max_length=100)     # TODO: Check if there's smoother way
    group = CustomModels.group_field()          # ^ and if necessary
    room = models.PositiveSmallIntegerField()   # ^^

#class for data from sensor to read last data?