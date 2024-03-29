from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# app_name = "Smart_Home"

urlpatterns = [
    path('API/rooms/', views.RoomListAPI.as_view(), name='RoomListAPI'),

    path('API/deviceRGB=<pk>', views.DeviceRGBDetailsAPI.as_view(), name='DeviceRGBDetails'),
    path('API/deviceRGB/', views.DeviceAPIListRGB.as_view(), name='DeviceAPIListRGB'),
    path('API/deviceOnOff=<pk>', views.DeviceOnOffDetails.as_view(), name='DeviceOnOffDetails'),
    path('API/deviceOnOff/', views.DeviceAPIListOnOff.as_view(), name='DeviceAPIListOnOff'),
    path('API/deviceProgrammed=<pk>', views.DeviceProgramDetails.as_view(), name='DeviceProgramDetails'),
    path('API/deviceProgrammed/', views.DeviceAPIListProgrammed.as_view(), name='DeviceAPIListProgrammed'),
    path('API/devicePercent=<pk>', views.DevicePercentDetails.as_view(), name='DevicePercentDetails'),
    path('API/devicePercent/', views.DeviceAPIListPercent.as_view(), name='DeviceAPIListPercent'),

    path('API/error/', views.ErrorDataListAPIView.as_view(), name='ErrorListAPI'),
    #For searching API/errors/?<field_name>=

    path('API/sensor=<pk>', views.SensorDetails.as_view(), name='SensorDetails'),
    path('API/sensor/', views.SensorListAPIView.as_view(), name='SensorListAPI'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
# TODO: Consider -Rename urlpatterns for clarity