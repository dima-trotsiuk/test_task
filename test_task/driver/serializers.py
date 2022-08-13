from rest_framework import serializers

from .models import Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('pk', 'first_name', 'last_name', 'created_at', 'updated_at')
