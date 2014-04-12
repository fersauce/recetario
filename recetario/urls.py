# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root':settings.MEDIA_ROOT}
        ),
    url(r'^sobre/$', 'principal.views.sobre'),
    url(r'^$', 'principal.views.inicio'),
    url(r'^usuarios/$', 'principal.views.usuarios'),
    url(r'^recetas/$', 'principal.views.listaRecetas'),
    url(r'^receta/(?P<idReceta>\d+)$', 'principal.views.detalleReceta'),
    url(r'^contacto/$', 'principal.views.contacto'),
    url(r'^receta/nueva/$', 'principal.views.nuevaReceta'),
    url(r'^comenta/$', 'principal.views.nuevoComentario'),
    url(r'^usuario/$', 'principal.views.usuario'),
    url(r'^usuario/nuevo/$', 'principal.views.usuarioNuevo'),
    url(r'^usuario/nuevopass/$', 'principal.views.recuperarPass'),
)
