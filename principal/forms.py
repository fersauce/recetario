'''
Created on 11/02/2014

@author: sauce
'''
from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from principal.models import Receta, Comentario, Usuario, Usuario2


class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tu correo electronico')
    mensaje = forms.CharField(widget=forms.Textarea)


class RecetaForm(ModelForm):
    class Meta:
        model = Receta


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario


class UsuarioForm(forms.Form):

    username = forms.CharField(label='Nombre de Usuario', required=True)
    email = forms.EmailField(label='correo', required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    nombre = forms.CharField(label='Nombres', required=True)
    #apellido = forms.CharField(label= 'Apellidos', required=True)
    #direccion = forms.CharField(label='Direccion', required=True)


class RecuperarPassForm(forms.Form):
    correo = forms.EmailField(label='Ingrese su correo')


class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario2
        fields = ('username', 'password', 'direccion', 'email')

    password = forms.ModelChoiceField(queryset='', widget=forms.PasswordInput())