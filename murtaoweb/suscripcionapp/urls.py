from django.conf.urls import url
from django.urls import path
from .views import suscripcion_ingreso, suscripcion_anular

# Create your views here.

urlpatterns = [
    path('', suscripcion_ingreso, name="suscripcion_ingreso"),
    path('anular/', suscripcion_anular, name="suscripcion_anular"),
]