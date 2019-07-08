from django.contrib import admin
from .models import RGBDevice , OnOffDevice, ProgramDevice, PercentDevice, Sensor

admin.site.register(RGBDevice)
admin.site.register(OnOffDevice)
admin.site.register(ProgramDevice)
admin.site.register(PercentDevice)
admin.site.register(Sensor)
