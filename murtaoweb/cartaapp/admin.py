from django.contrib import admin
from .models import Carta, CartaRestoran

# Register your models here.


class CartaRestoranAdmin(admin.ModelAdmin):
    list_display = ('numero_id','estado','creado')
    list_filter = ('estado', 'creado')

admin.site.register(CartaRestoran, CartaRestoranAdmin)

class CartaAdmin(admin.ModelAdmin):
    list_display = ('numero_id','estado','creado')
    list_filter = ('estado', 'creado')

admin.site.register(Carta, CartaAdmin)


