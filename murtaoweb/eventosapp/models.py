from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.

class Evento(models.Model):
    STATUS_CHOICES = (
        ('Borrador', 'Borrador'),
        ('Publicado', 'Publicado')
    )
    estado = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Borrador')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField()
    imagen = models.ImageField(null=True, blank=True)
    link = models.CharField(max_length=500,null=True, blank=True)
    slug = models.SlugField(editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre