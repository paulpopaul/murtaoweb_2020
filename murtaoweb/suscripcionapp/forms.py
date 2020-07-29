from django import forms
from crispy_forms.helper import FormHelper
from .models import SuscripcionUsuario, Suscripcion

# Register your models here.

class SuscripcionUsuarioIngresoForm(forms.ModelForm):

    nombre = forms.CharField(label='nombre',widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Nombre'}
    ))

    apellido = forms.CharField(label='nombre',widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Apellido'}
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder': ' Email'}
    ))

    telefono = forms.CharField(label='nombre',widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Teléfono'}
    ))

    ciudad = forms.CharField(label='nombre',widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Ciudad'}
    ))


    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = SuscripcionUsuario
        fields = ['nombre', 'apellido','email','telefono','f_nacimiento','ciudad']
        widgets = {
            'f_nacimiento': forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'Fecha de Nacimiento'}),
        }

        def clean_email(self):
            email = self.clean_data.get('email')

            return email

class SuscripcionCreacionForm(forms.ModelForm):
    class Meta:
        model = Suscripcion
        fields = ['subject','body','email', 'status']