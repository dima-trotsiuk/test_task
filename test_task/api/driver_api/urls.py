from django.urls import path

from .views import DriverAPIListCreate, DriverAPIRetrieveUpdateDestroy

driver_urlpatterns = [
    path('driver/', DriverAPIListCreate.as_view()),
    path('driver/<int:pk>/', DriverAPIRetrieveUpdateDestroy.as_view()),
]
