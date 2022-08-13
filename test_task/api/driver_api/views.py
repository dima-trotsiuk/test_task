from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from driver.models import Driver
from driver.service import DriverFilter
from .serializers import DriverSerializer


class DriverAPIListCreate(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DriverFilter


class DriverAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
