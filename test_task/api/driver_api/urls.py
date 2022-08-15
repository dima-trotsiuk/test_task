from django.urls import path

from .views import DriverAPIListCreate, DriverAPIRetrieveUpdateDestroy

driver_urlpatterns = [
    path('driver/', DriverAPIListCreate.as_view(), name='list_drivers'),
    path('driver/<int:pk>/', DriverAPIRetrieveUpdateDestroy.as_view(), name='detail_driver'),
]
