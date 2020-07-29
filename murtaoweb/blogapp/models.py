from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    ESTADO = (
        ('Borrador', 'Borrador'),
        ('Publicado', 'Publicado')
    )
    estado = models.CharField(max_length=12, choices=ESTADO, default='Borrador')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    imagen_blog = models.ImageField()
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_blog = models.DateField(default=timezone.now)
    hora_blog = models.TimeField(default=timezone.now)
    linkblog = models.CharField(max_length=255, null=True, blank=True)
    video_blog = models.CharField(max_length=255, null=True, blank=True)
    seo_descripcion = models.CharField(max_length=165,null=True, blank=True)
    slug = models.SlugField(editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo