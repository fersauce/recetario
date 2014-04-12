# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    """
    Clase que representa a una receta
    """
    __tablename__ = 'receta'
    titulo = models.CharField(max_length=100, unique=True)
    ingredientes = models.TextField(help_text='Redacta los ingredientes')
    preparacion = models.TextField(verbose_name='Preparación')
    imagen = models.ImageField(upload_to='recetas', verbose_name='Imágen')
    tiempoRegistro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.titulo
    
class Comentario(models.Model):
    """
    Clase que representa a un comentario de una receta
    """
    __tablename__ = 'comentario'
    receta = models.ForeignKey(Receta)
    texto = models.TextField(help_text='Tu comentario',
                             verbose_name='comentario')
    def __unicode__(self):
        return self.texto


class Usuario(models.Model):
    class Meta:
        db_table = 'usuarios'


    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    nombre = models.CharField(max_length=40)



class Usuario2(User):
    direccion = models.CharField(max_length=50)
