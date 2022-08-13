from django.urls import path, include
from .driver_api.urls import driver_urlpatterns


urlpatterns = [
    path('drivers/', include(driver_urlpatterns))
]
