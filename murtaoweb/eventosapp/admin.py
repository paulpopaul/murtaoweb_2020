from django.contrib import admin
from .models import Evento
# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'lugar', 'fecha', 'hora','creado')
    list_filter = ('nombre','fecha')
    search_fields = ('nombre','descripcion')

admin.site.register(Evento, EventosAdmin)