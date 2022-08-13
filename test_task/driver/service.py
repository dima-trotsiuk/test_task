from django_filters import rest_framework as filters

from .models import Driver


class DriverFilter(filters.FilterSet):
    created_at = filters.DateFilter(input_formats=["%d/%m/%Y"])

    class Meta:
        model = Driver
        fields = {
            'created_at': ['gte', 'lte']
        }
