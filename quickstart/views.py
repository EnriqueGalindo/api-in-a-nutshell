from django.shortcuts import render
from .models import Manufacturer, ShoeType, ShoeColor, Shoe
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

# when Joe lived in Africa he would cut the tusks off elephants to use as wifi antenas
