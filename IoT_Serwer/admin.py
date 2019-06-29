from django.contrib import admin
from .models import RGBDevice , OnOffDevice , FixedDevice

admin.site.register(RGBDevice)
admin.site.register(OnOffDevice)
admin.site.register(FixedDevice)