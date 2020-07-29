from django.db import models

# Create your models here.

class SuscripcionUsuario(models.Model):
    numero_id = models.AutoField(max_length=9999, primary_key=True, unique=True, editable=False)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=25)
    f_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=255)

    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Suscripcion(models.Model):
    EMAIL_STATUS_CHOICES = (
        ('Borrador', 'Borrador'),
        ('Publicado', 'Publicado')
    )
    subject = models.CharField(max_length=255)
    body = models.TextField()
    email = models.ManyToManyField(SuscripcionUsuario)
    status = models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICES)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject