from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Reserva(models.Model):

    nombre_persona = models.CharField(max_length=255, verbose_name="Nombre contacto")
    email = models.EmailField(verbose_name="Email contacto")
    fecha_evento = models.DateField(verbose_name="Fecha Reserva")
    hora_evento = models.TimeField(verbose_name="Hora Reserva")
    numeros_invitados = models.CharField(max_length=25,verbose_name="Número Invitados")
    telefono_invitado = models.CharField(max_length=25, verbose_name="Telefóno contacto")
    mensaje_evento = models.TextField(verbose_name="Mensaje")
    reserva_realizada = models.BooleanField(default=False, verbose_name="Realizada?")

    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.nombre_persona

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre_persona)
        super(Reserva, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ['fecha_evento']