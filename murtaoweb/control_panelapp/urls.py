from django.urls import path

from suscripcionapp.views import control_suscripcion, control_suscripcion_lista, control_suscripcion_detalle, \
    control_suscripcion_editar, control_suscripcion_eliminar


urlpatterns = [
    path('suscripcion/', control_suscripcion, name="control_suscripcion"),
    path('suscripcion-lista/', control_suscripcion_lista, name="control_suscripcion_lista"),
    path('suscripcion-detalle/<int:pk>/', control_suscripcion_detalle, name="control_suscripcion_detalle"),
    path('suscripcion-editar/<int:pk>/', control_suscripcion_editar, name="control_suscripcion_editar"),
    path('suscripcion-eliminar/<int:pk>/', control_suscripcion_eliminar, name="control_suscripcion_eliminar"),

]

