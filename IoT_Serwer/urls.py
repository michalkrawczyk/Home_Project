from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# app_name = "Smart_Home"

urlpatterns = [
    # path('deviceRGB=<pk>', views.DeviceRGBDetails.as_view(), name='DeviceRGBDetails'),
    # path('deviceOnOff=<pk>', views.DeviceOnOffDetails.as_view(), name='DeviceOnOffDetails'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
