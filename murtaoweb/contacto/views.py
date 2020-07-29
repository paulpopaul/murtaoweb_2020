from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from .forms import ContactoForm
from reservasapp.forms import ReservaForm
# Create your models here.

def contacto(request):
    if request.method == "POST":
        contact = ContactoForm(request.POST or None)
        redirect_to = '/enviando/'

        if contact.is_valid():
            instance = contact.save(commit=False)
            instance.save()
            to_mail = [instance.email]
            subject = "Web Mail Murtao"
            from_email = settings.DEFAULT_FROM_EMAIL
            context = {
                'nombre': instance.nombre,
                'apellido': instance.apellido,
                'celular': instance.celular,
                'email': instance.email,
                'mensaje': instance.mensaje
            }
            with open(settings.BASE_DIR + "/templates/contactoapp/contacto_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("contactoapp/contacto_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            subject = "Copia: Web Mail Murtao"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_mail = ['contacto@murtao.cl']
            with open(settings.BASE_DIR + "/templates/contactoapp/contacto_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("contactoapp/contacto_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            return redirect(redirect_to)
    else:
        contact = ContactoForm()
    return contact

'''

def contacto(request):
    if request.method == "POST":
        contact = ContactoForm(request.POST or None)
        redirect_to = '/enviando/'

        if contact.is_valid():
            instance = contact.save(commit=False)
            instance.save()
            to_mail = [instance.email]
            subject = "Solicitud de Contacto"
            from_email = settings.EMAIL_HOST_USER
            context = {
                'nombre': instance.nombre,
                'apellido': instance.apellido,
                'celular': instance.celular,
                'email': instance.email,
                'mensaje': instance.mensaje
            }
            with open(settings.BASE_DIR + "/templates/contactoapp/contacto_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("contactoapp/contacto_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            subject = "Solicitud de Contacto"
            from_email = settings.EMAIL_HOST_USER
            to_mail = ['ainsworth.developed@gmail.com']
            with open(settings.BASE_DIR + "/templates/contactoapp/contacto_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("contactoapp/contacto_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            return redirect(redirect_to)
    else:
        contact = ContactoForm()

    context = {
        'contact': contact,
    }
    template = "contactoapp/contacto_template.html"
    return render(request, template, context)

'''