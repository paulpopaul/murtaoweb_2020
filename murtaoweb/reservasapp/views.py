from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template

from suscripcionapp.models import SuscripcionUsuario, Suscripcion
from suscripcionapp.forms import SuscripcionUsuarioIngresoForm, SuscripcionCreacionForm

from .forms import ReservaForm
# Create your models here.

def reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST or None)
        redirect_to = '/redirect/'

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            to_mail = [instance.email]
            subject = "Solicitud de Reserva"
            from_email = settings.DEFAULT_FROM_EMAIL
            context = {
                'nombre_persona': instance.nombre_persona,
                'email': instance.email,
                'fecha_evento': instance.fecha_evento,
                'hora_evento': instance.hora_evento,
                'numeros_invitados': instance.numeros_invitados,
                'telefono_invitado': instance.telefono_invitado,
                'mensaje_evento': instance.mensaje_evento,
                'reserva_realizada': instance.reserva_realizada
            }
            with open(settings.BASE_DIR + "/templates/reservasapp/reserva_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("reservasapp/reserva_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            subject = "Solicitud de Reserva"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_mail = ['contacto@murtao.cl']
            with open(settings.BASE_DIR + "/templates/reservasapp/reserva_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("reservasapp/reserva_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            return redirect(redirect_to)
    else:
        form = ReservaForm()
    return form

from contacto.forms import ContactoForm
# Create your models here.

def contacto(request):
    if request.method == "POST":
        contact = ContactoForm(request.POST or None)
        enviando = '/enviando/'

        if contact.is_valid():
            instance = contact.save(commit=False)
            instance.save()
            to_mail = [instance.email]
            subject = "Copia: Nuevo Mensaje | Murtao Web Mail"
            from_email = settings.DEFAULT_FROM_EMAIL
            context = {
                'nombre': instance.nombre,
                'apellido': instance.apellido,
                'celular': instance.celular,
                'email': instance.email,
                'mensaje': instance.mensaje,
                'fecha':instance.fecha,
            }
            with open(settings.BASE_DIR + "/templates/contactoapp/contacto_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("contactoapp/contacto_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            subject = "Copia: Nuevo Mensaje | Murtao Web Mail"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_mail = ['contacto@murtao.cl']
            with open(settings.BASE_DIR + "/templates/contactoapp/contacto_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("contactoapp/contacto_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            return redirect(enviando)
    else:
        contact = ContactoForm()
    return contact


def suscripcion_ingreso(request):
    suscripcion = SuscripcionUsuarioIngresoForm(request.POST or None)
    enviando = '/enviando/'
    if suscripcion.is_valid():
        instance = suscripcion.save(commit=False)
        if SuscripcionUsuario.objects.filter(email=instance.email).exists():
            messages.warning(request,
                             'Your Mail arleady exist in our database',
                             "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request,
                             'Your Email has been sbmitted to the database',
                             "alert alert-success alert-dismissible")

            subject = "Gracias por Suscribirte"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/templates/suscripcionapp/ingresar_email_template.txt") as f:
                signup_message = f.read()

            html_template = get_template("suscripcionapp/ingresar_email_template.html").render()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            message.attach_alternative(html_template, "text/html")
            message.send()

            subject = "Suscripcion Nueva"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_mail = ['contacto@murtao.cl']
            with open(settings.BASE_DIR + "/templates/suscripcionapp/ingresar_email_template.txt") as f:
                signup_message = f.read()
            html_template = get_template("suscripcionapp/ingresar_email_template.html").render()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            return redirect(enviando)
    else:
        suscripcion = SuscripcionUsuarioIngresoForm()
    return suscripcion

'''
def reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST or None)
        redirect_to = '/redirect/'

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            to_mail = [instance.email]
            subject = "Solicitud de Reserva"
            from_email = settings.EMAIL_HOST_USER
            context = {
                'nombre_persona': instance.nombre_persona,
                'email': instance.email,
                'fecha_evento': instance.fecha_evento,
                'hora_evento': instance.hora_evento,
                'numeros_invitados': instance.numeros_invitados,
                'telefono_invitado': instance.telefono_invitado,
                'mensaje_evento': instance.mensaje_evento,
                'reserva_realizada': instance.reserva_realizada
            }
            with open(settings.BASE_DIR + "/templates/reservasapp/reserva_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("reservasapp/reserva_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            subject = "Solicitud de Reserva"
            from_email = settings.EMAIL_HOST_USER
            to_mail = ['ainsworth.developed@gmail.com']
            with open(settings.BASE_DIR + "/templates/reservasapp/reserva_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("reservasapp/reserva_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            return redirect(redirect_to)
    else:
        form = ReservaForm()

    context = {
        'form': form,
    }
    template = "index.html"
    return render(request, template, context)
'''