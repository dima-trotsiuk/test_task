from django.urls import path

from .api import DriverAPIListCreate, DriverAPIRetrieveUpdateDestroy


urlpatterns = [
    path('driver/', DriverAPIListCreate.as_view()),
    path('driver/<int:pk>/', DriverAPIRetrieveUpdateDestroy.as_view()),
]
