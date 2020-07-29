"""murtaoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from murtaoweb import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', include(('blogapp.urls', 'blogapp'), namespace='blogapp')),
    path('eventos/', include(('eventosapp.urls', 'eventosapp'), namespace='eventosapp')),
    path('menu/', include(('menuapp.urls', 'menuapp'), namespace='menuapp')),
    path('contacto/', include(('contacto.urls', 'contacto'), namespace='contacto')),
    path('control/', include(('control_panelapp.urls', 'control_panelapp'), namespace='control_panelapp')),
    path('reservas/', include(('reservasapp.urls', 'reservasapp'), namespace='reservasapp')),
    path('suscripcion/', include(('suscripcionapp.urls', 'suscripcionapp'), namespace='suscripcionapp')),
    path('enviando/', TemplateView.as_view(template_name="reservasapp/contacto_enviando.html")),
    path('redirect/', TemplateView.as_view(template_name="reservasapp/reserva_redirect.html"))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
