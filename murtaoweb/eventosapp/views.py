from django.shortcuts import render, get_list_or_404

from .models import Evento
# Create your Views here.

def evento_list(request):
    objects_list = Evento.objects.order_by('fecha').filter(estado='Publicado')
    context = {
        'objects_list': objects_list,
    }
    template = 'eventosapp/evento_list.html'
    return render(request, template, context)

def evento_detail(request, slug):
    template = 'eventosapp/evento_detail.html'
    evento = get_list_or_404(Evento, slug=slug)
    context = {
        'evento': evento,
    }
    return render(request,template,context)

