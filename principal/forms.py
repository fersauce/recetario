'''
Created on 11/02/2014

@author: sauce
'''
from django import forms

class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tu correo electronico')
    mensaje = forms.CharField(widget=forms.Textarea)
    