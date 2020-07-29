from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','estado','creado')
    list_filter = ('titulo', 'estado', 'fecha_blog')
    search_fields = ('titulo', 'descripcion','seo_descripcion')

admin.site.register(Post, PostAdmin)