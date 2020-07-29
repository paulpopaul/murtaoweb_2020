from django.contrib import admin
from .models import Instagram
# Register your models here.
class InstagramAdmin(admin.ModelAdmin):
    list_display = ('numero_id','estado','creado')
    list_filter = ('estado', 'creado')

admin.site.register(Instagram, InstagramAdmin)