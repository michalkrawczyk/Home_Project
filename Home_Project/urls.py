"""Home_Project URL Configuration

    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', include('IoT_Serwer.urls')),
]
