from django.shortcuts import render, get_list_or_404
from reservasapp import views

from eventosapp.models import Evento
from blogapp.models import Post
from menuapp.models import Menu, Categoria
from instaapp.models import Instagram
from galeriaapp.models import Imagen
from cartaapp.models import Carta, CartaRestoran

def home(request):
    objects_list = Evento.objects.order_by('fecha').filter(estado='Publicado')[:8]
    post_list = Post.objects.order_by('-creado').filter(estado='Publicado')
    menu1 = Categoria.objects.filter(estado='Publicado', id=1)
    cat1 = Menu.objects.filter(estado='Publicado', categoria=1)
    cat2 = Menu.objects.filter(estado='Publicado', categoria=2)
    cat3 = Menu.objects.filter(estado='Publicado', categoria=3)
    cat4 = Menu.objects.filter(estado='Publicado', categoria=4)
    cat5 = Menu.objects.filter(estado='Publicado', categoria=5)
    cat6 = Menu.objects.filter(estado='Publicado', categoria=6)
    cat7 = Menu.objects.filter(estado='Publicado', categoria=7)
    cat8 = Menu.objects.filter(estado='Publicado', categoria=8)
    cat9 = Menu.objects.filter(estado='Publicado', categoria=9)
    cat10 = Menu.objects.filter(estado='Publicado', categoria=10)

    img = Imagen.objects.filter(estado='Publicado')
    cartarestoran = CartaRestoran.objects.filter(estado='Publicado')
    carta = Carta.objects.filter(estado='Publicado')

    insta = Instagram.objects.filter(estado='Publicado')
    context = {
        'form': views.reserva(request=request),
        'contact': views.contacto(request=request),
        'suscripcion':views.suscripcion_ingreso(request=request),
        'objects_list': objects_list,
        'post_list': post_list,

        'menu1': menu1,
        'cat1': cat1,
        'cat2': cat2,
        'cat3': cat3,
        'cat4': cat4,
        'cat5': cat5,
        'cat6': cat6,
        'cat7': cat7,
        'cat8': cat8,
        'cat9': cat9,
        'cat10': cat10,

        'img' : img,
        'cartarestoran': cartarestoran,
        'carta': carta,
        'insta':insta,
    }
    template = 'index.html'
    return render(request, template, context)

