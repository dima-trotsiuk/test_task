from django.db import models
from driver.models import Driver


class Vehicle(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    make = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    plate_number = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk} = {self.plate_number}"
