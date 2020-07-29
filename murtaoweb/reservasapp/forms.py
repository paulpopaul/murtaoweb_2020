from django import forms
from .models import Reserva

# Create your models here.

class ReservaForm(forms.ModelForm):

    nombre_persona = forms.CharField(label='Nombre contacto',widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control'}
    ))

    numeros_invitados = forms.CharField(label='Número Invitados',widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))

    telefono_invitado = forms.CharField(label='Telefóno contacto', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    mensaje_evento = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '5', 'rows': '10', 'class': 'form-control'}
    ))

    class Meta:
        model = Reserva
        fields = ('nombre_persona', 'email', 'fecha_evento', 'hora_evento',
                  'numeros_invitados','telefono_invitado','mensaje_evento')
        widgets = {
            'fecha_evento': forms.DateInput(attrs={'class': 'datepicker'}),
            'hora_evento': forms.DateTimeInput(attrs={'class': 'timepicker'})
        }

