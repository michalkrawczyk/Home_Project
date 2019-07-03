from django.contrib import admin
from .models import RGBDevice , OnOffDevice, ProgramDevice, PercentDevice

admin.site.register(RGBDevice)
admin.site.register(OnOffDevice)
admin.site.register(ProgramDevice)
admin.site.register(PercentDevice)
