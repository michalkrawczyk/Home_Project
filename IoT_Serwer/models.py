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


class Room(models.Model):
    name = models.TextField(max_length=100)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk) + " - " + self.name


class Device(models.Model):
    name = models.TextField(max_length=100)
    group = CustomModels.group_field()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    manualControl = models.BooleanField(default=False)
    errorState = models.BooleanField(default=False)
    lastChange = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        abstract = True


class RGBDevice(Device):
    red = CustomModels.color_field()
    blue = CustomModels.color_field()
    green = CustomModels.color_field()


class OnOffDevice(Device):
    turnedON = models.BooleanField(default=False)


class ProgramDevice(Device):  # for devices with specified programs
    program = models.PositiveSmallIntegerField(default=0)


class PercentDevice(Device):
    data = CustomModels.percentage_field()
# Space for new types of Devices


class ErrorData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    code = models.SmallIntegerField()
    name = models.TextField(max_length=100)
    group = CustomModels.group_field()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Sensor(Device):
    data = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        default=0
    )  # max 999999.9999
    manualControl = None

#TODO : Future: Tables for History