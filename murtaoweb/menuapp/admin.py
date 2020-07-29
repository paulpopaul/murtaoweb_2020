from django.contrib import admin
from .models import Categoria, Menu

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado','id')
    list_filter = ('titulo', 'estado')
    search_fields = ('titulo', 'contenido')
    readonly_fields = ('id',)
admin.site.register(Categoria, CategoriaAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'valor', 'estado', 'creado')
    list_filter = ('titulo', 'categoria', 'valor', 'estado')
    search_fields = ('titulo', 'valor', 'contenido')
admin.site.register(Menu, MenuAdmin)