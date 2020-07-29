from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Categoria(models.Model):
    ESTADO = (
        ('Borrador', 'Borrador'),
        ('Publicado', 'Publicado')
    )
    estado = models.CharField(max_length=12, choices=ESTADO, default='Borrador')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(blank=True, null=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(max_length=255, blank=True, null=True)
    slug = models.SlugField(editable=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Menu(models.Model):
    ESTADO = (
        ('Borrador', 'Borrador'),
        ('Publicado', 'Publicado')
    )
    estado = models.CharField(max_length=12, choices=ESTADO, default='Borrador')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(blank=True, null=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(blank=True, null=True)
    valor = models.CharField(max_length=255)
    slug = models.SlugField(editable=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

