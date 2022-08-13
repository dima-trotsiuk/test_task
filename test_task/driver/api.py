from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Driver
from .serializers import DriverSerializer
from .service import DriverFilter


class DriverAPIListCreate(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DriverFilter


class DriverAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
