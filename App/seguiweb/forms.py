"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView
from App.post.models import Post
from App.seguiweb.models import Seguimientos




class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Usuario'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ingresoform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Procedencia','StartedOn','RUT','Nombre','Apellido_Paterno','Apellido_Materno','Fecha_de_nacimiento',
                  'Email_de_contacto','Telefono_movil','Telefono_fijo','Isapre','Seguro_complementario',
                  'Codigo_de_intervencion','Nombre_de_la_intervencion','Medico_tratante','Fecha_probable_de_Hospitalizacion'
                  ]


class editarform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Procedencia','StartedOn','RUT','Nombre','Apellido_Paterno','Apellido_Materno','Fecha_de_nacimiento',
                  'Email_de_contacto','Telefono_movil','Telefono_fijo','Isapre','Seguro_complementario',
                  'Codigo_de_intervencion','Nombre_de_la_intervencion','Medico_tratante','Fecha_probable_de_Hospitalizacion'

                  ]

class eventosform(forms.ModelForm):
    class Meta:
         model = Seguimientos
         fields = ['id','texto_evento'
                  ]



