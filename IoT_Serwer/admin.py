from django.contrib import admin

from .models import (
    Room,
    RGBDevice, OnOffDevice, ProgramDevice, PercentDevice, Sensor
    )


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'enabled', )
    list_filter = ('enabled',)


admin.site.register(Room, RoomAdmin)

admin.site.register(RGBDevice)
admin.site.register(OnOffDevice)
admin.site.register(ProgramDevice)
admin.site.register(PercentDevice)
admin.site.register(Sensor)

#TODO :list displays and filters for Devices

