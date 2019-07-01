from django.contrib import admin
from .models import RGBDevice , OnOffDevice, FixedDevice, ProgramDevice

admin.site.register(RGBDevice)
admin.site.register(OnOffDevice)
admin.site.register(FixedDevice)
admin.site.register(ProgramDevice)
