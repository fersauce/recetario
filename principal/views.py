from django.shortcuts import render_to_response, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.template.context import RequestContext
from principal.forms import ContactoForm
from django.core.mail.message import EmailMessage

def sobre(request):
    html='<html><body>Proyecto de Ejemplo en MDW</body></html>'
    return HttpResponse(html)

def inicio(request):
    recetas = Receta.objects.all()
    return render_to_response('inicio.html',{'recetas':recetas})

def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    return render_to_response('usuarios.html', {'usuarios':usuarios,
                                                'recetas':recetas})
    
def listaRecetas(request):
    recetas = Receta.objects.all()
    return render_to_response('recetas.html', {'datos':recetas},
                              context_instance = RequestContext(request))
    
def detalleReceta(request, idReceta):
    dato = get_object_or_404(Receta, pk=idReceta)
    comentarios = Comentario.objects.filter(receta=dato)
    return render_to_response('receta.html', {'receta':dato,
                                              'comentarios':comentarios},
                              context_instance=RequestContext(request))

def contacto(request):
    if(request.method == 'POST'):
        formulario = ContactoForm(request.POST)
        if(formulario.is_valid()):
            titulo = 'Mensaje desde el recetario de MDW'
            contenido = formulario.cleaned_data['mensaje']+"\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido,
                                  to=['carlifer.fernando@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('contactoform.html', {'formulario':formulario},
                              context_instance = RequestContext(request))

