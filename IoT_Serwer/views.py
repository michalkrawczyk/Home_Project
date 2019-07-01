from django.shortcuts import get_object_or_404
# from .models import RGBDevice, OnOffDevice , FixedDevice , ProgramDevice

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


class DeviceRGBDetails(APIView):
    def get_object(self, pk):
        return get_object_or_404(RGBDevice)

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SerializerRGB(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SerializerRGB(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceOnOffDetails(APIView):
    def get_object(self, pk):
        return get_object_or_404(OnOffDevice)

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SerializerOnOff(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SerializerOnOff(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceFixedDetails(APIView):
    def get_object(self, pk):
        return get_object_or_404(FixedDevice)

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SerializerFixed(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SerializerFixed(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceProgramDetails(APIView):
    def get_object(self, pk):
        return get_object_or_404(ProgramDevice)

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SerializerProgrammed(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SerializerProgrammed(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TODO: View for ERROR DATA
