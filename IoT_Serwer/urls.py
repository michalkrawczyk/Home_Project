from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# app_name = "Smart_Home"

urlpatterns = [
    path('API/deviceRGB=<pk>', views.DeviceRGBDetails.as_view(), name='DeviceRGBDetails'),
    path('API/deviceOnOff=<pk>', views.DeviceOnOffDetails.as_view(), name='DeviceOnOffDetails'),
    path('API/devicePercent=<pk>', views.DevicePercentDetails.as_view(), name='DevicePercentDetails'),
    path('API/deviceProgrammed=<pk>', views.DeviceProgramDetails.as_view(), name='DeviceProgramDetails'),

    path('API/error=<pk>', views.ErrorDataDetails.as_view(), name='ErrorDetails'),
    path('API/errors/', views.ErrorDataListAPIView.as_view(), name='ErrorListAPI'),
    #For searching API/errors/?<type>=

    path('API/sensor=<pk>', views.SensorDetails.as_view(), name='SensorDetails'),  # Consider other filter
]
urlpatterns = format_suffix_patterns(urlpatterns)
# TODO: Rename urlpatterns for clarity