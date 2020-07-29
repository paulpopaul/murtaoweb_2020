from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt,csrf_protect


from .models import SuscripcionUsuario, Suscripcion
from .forms import SuscripcionUsuarioIngresoForm, SuscripcionCreacionForm

# Create your views here.
@csrf_exempt
def suscripcion_ingreso(request):
    form = SuscripcionUsuarioIngresoForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if SuscripcionUsuario.objects.filter(email=instance.email).exists():
            messages.warning(request,
                             'Email existente en nuestra Base de Datos',
                             "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request,
                             'Suscripción realizada con éxito !',
                             "alert alert-success alert-dismissible")
            
            subject = instance.nombre + " bienvenido a Murtao"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [instance.email]
            context = {
                'numero_id': instance.numero_id,
                'nombre': instance.nombre,
                'apellido': instance.apellido,
                'telefono': instance.telefono,
                'email': instance.email,
                'f_nacimiento': instance.f_nacimiento,
                'ciudad': instance.ciudad,
                'create': instance.create
            }
            with open(settings.BASE_DIR + "/templates/suscripcionapp/ingresar_email_template.txt") as f:
                signup_message = f.read()

            html_template = get_template("suscripcionapp/ingresar_email_template.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            message.attach_alternative(html_template, "text/html")
            message.send()

            subject = "Suscripcion Nueva"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_mail = ['contacto@murtao.cl']
            with open(settings.BASE_DIR + "/templates/suscripcionapp/ingresar_email_template.txt") as f:
                signup_message = f.read()
            html_template = get_template("suscripcionapp/ingresar_email_template.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

    context = {
        'form':form,
    }
    template = "suscripcionapp/ingresar_email.html"
    return render(request,template,context)


def suscripcion_anular(request):
    form = SuscripcionUsuarioIngresoForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if SuscripcionUsuario.objects.filter(email=instance.email).exists():
            SuscripcionUsuario.objects.filter(email=instance.email).delete()
            messages.success(request,
                             'Tu correo electrónico ha sido eliminado',
                             "alert alert-success alert-dismissible")

            subject = "Disculpa por las molestias"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/templates/suscripcionapp/anular_email_template.txt") as f:
                signup_message = f.read()

            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("suscripcionapp/anular_email_template.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()

        else:
            messages.warning(request,
                             'Tu correo electronico no se encuentra en nuestra base de datos',
                             "alert alert-warning alert-dismissible")

    context = {
        "form":form,
    }
    template = "suscripcionapp/anular_email.html"
    return render(request, template, context)


def control_suscripcion(request):
    form = SuscripcionCreacionForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        suscripcion = Suscripcion.objects.get(id=instance.id)
        if suscripcion.status == "Publicado":
            subject = suscripcion.subject
            from_email = settings.DEFAULT_FROM_EMAIL
            for email in suscripcion.email.all():
                with open(settings.BASE_DIR + "/templates/contactoapp/contacto_template_detail.txt") as f:
                    signup_message = f.read()
                html_template = get_template("contactoapp/contacto_template_detail.html").render()
                message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=[email.email])
                message.attach_alternative(html_template, "text/html")
                message.send()
    context = {
        "form":form,
    }
    template = "control_panelapp/control_suscripcion.html"
    return render(request, template, context)


def control_suscripcion_lista(request):
    suscripcion = Suscripcion.objects.all().order_by('-id')[:3]
    paginator = Paginator(suscripcion, 10)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <=max_index -5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    context = {
        "items": items,
        "page_range":page_range
    }
    template = "control_panelapp/control_suscripcion_lista.html"
    return render(request, template, context)


def control_suscripcion_detalle(request, pk):
    suscripcion = get_object_or_404(Suscripcion, pk=pk)

    context = {
        "suscripcion":suscripcion,
    }
    template = "control_panelapp/control_suscripcion_detalle.html"
    return render(request, template, context)


def control_suscripcion_editar(request, pk):
    suscripcion = get_object_or_404(Suscripcion, pk=pk)

    if request.method == 'POST':
        form = SuscripcionCreacionForm(request.POST, instance=suscripcion)

        if form.is_valid():
            suscripcion = form.save()

            if suscripcion.status == "Publicado":
                subject = suscripcion.subject
                body = suscripcion.body
                from_email = settings.DEFAULT_FROM_EMAIL
                for email in suscripcion.email.all():
                    send_mail(subject=subject, from_email=from_email, recipient_list=[email.email], message=body, fail_silently=True)

            return redirect('control_panelapp:control_suscripcion_detalle', pk=suscripcion.pk)
    else:
        form = SuscripcionCreacionForm(instance=suscripcion)

    context = {
        "form":form
    }
    template = "control_panelapp/control_suscripcion.html"

    return render(request, template, context)


def control_suscripcion_eliminar(request, pk):
    suscripcion = get_object_or_404(Suscripcion, pk=pk)

    if request.method == 'POST':
        form = SuscripcionCreacionForm(request.POST, instance=suscripcion)

        if form.is_valid():
            suscripcion.delete()
            return redirect('control_panelapp:control_suscripcion_lista')

    else:
        form = SuscripcionCreacionForm(instance=suscripcion)

    context = {
        'form': form,
    }
    template = 'control_panelapp/control_suscripcion_eliminar.html'

    return render(request, template, context)