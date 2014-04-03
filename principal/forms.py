'''
Created on 11/02/2014

@author: sauce
'''
from django import forms
from django.forms.models import ModelForm
from principal.models import Receta, Comentario


class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tu correo electronico')
    mensaje = forms.CharField(widget=forms.Textarea)

class RecetaForm(ModelForm):
    class Meta:
        model = Receta

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario