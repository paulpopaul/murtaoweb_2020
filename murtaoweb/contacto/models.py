# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Contacto(models.Model):
    fecha = models.DateTimeField(_('fecha'), auto_now=True, blank=True, null=True, )
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    celular = models.CharField('Teléfono', max_length=13)
    email = models.EmailField('Email')
    mensaje = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['fecha']

