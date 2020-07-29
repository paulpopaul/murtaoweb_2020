from django.urls import path
from .views import reserva

# Create your views here.

urlpatterns = [
    path('', reserva, name="reserva"),
]