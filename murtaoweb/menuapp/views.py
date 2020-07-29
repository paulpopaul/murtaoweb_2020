from django.shortcuts import render, get_object_or_404
from .models import Menu, Categoria
# Create your views here.

def menu_list(request):
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
    context = {
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
    }
    template = 'menuapp/menu_list.html'
    return render(request, template, context)


def menu_detail(request, slug):
    menus = get_object_or_404(Menu, slug=slug)
    context = {
        'menus': menus,
    }
    template = 'menuapp/menu_detail.html'
    return render(request, template, context)


def menu_category(request, slug):
    template = 'menuapp/menu_category.html'
    categoria = get_object_or_404(Categoria, slug=slug)
    menu = Menu.objects.filter(categoria=categoria, estado='Publicado')
    context = {
        'categoria':categoria,
        'menu':menu,
    }
    return render(request,template,context)