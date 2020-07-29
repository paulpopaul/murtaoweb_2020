from django.db import models

# Create your models here.

class Instagram(models.Model):

    ESTADO = {
        ('Publicado', 'Publicado'),
        ('Borrador', 'Borrador')
    }
    estado = models.CharField(max_length=12, choices=ESTADO, default='Publicado')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    imagen = models.ImageField()
    numero_id = models.AutoField(max_length=9999, primary_key=True, unique=True)
    slug = models.SlugField(editable=False, unique=True)

    def save(self, *args, **kwargs):
        super(Instagram, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = self.numero_id
            self.save()

    def __str__(self):
        return str(self.numero_id)
