import email
from random import choice
import string
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render_to_response, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from principal.models import Receta, Comentario, Usuario
from django.contrib.auth.models import User
from django.template.context import RequestContext
from principal.forms import ContactoForm, RecetaForm, ComentarioForm, UsuarioForm, RecuperarPassForm, UserForm
from django.core.mail.message import EmailMessage


def sobre(request):
    html = '<html><body>Proyecto de Ejemplo en MDW</body></html>'
    return HttpResponse(html)


def inicio(request):
    recetas = Receta.objects.all()
    return render_to_response('inicio.html', {'recetas': recetas}, context_instance=RequestContext(request))


def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuarios,
                                                'recetas': recetas}, context_instance=RequestContext(request))


def listaRecetas(request):
    recetas = Receta.objects.all()
    return render_to_response('recetas.html', {'datos': recetas},
                              context_instance=RequestContext(request))
def detalleReceta(request, idReceta):
    dato = get_object_or_404(Receta, pk=idReceta)
    comentarios = Comentario.objects.filter(receta=dato)
    return render_to_response('receta.html', {'receta': dato,
                                              'comentarios': comentarios},
                              context_instance=RequestContext(request))


def contacto(request):
    if (request.method == 'POST'):
        formulario = ContactoForm(request.POST)
        if (formulario.is_valid()):
            titulo = 'Mensaje desde el recetario de MDW'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido,
                                  to=['carlifer.fernando@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/', context_instance=RequestContext(request))
    else:
        formulario = ContactoForm()
    return render_to_response('comentarioform.html', {'formulario': formulario},
                              context_instance=RequestContext(request))


def nuevaReceta(request):
    if request.method == 'POST':
        formulario = RecetaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas', context_instance=RequestContext(request))
    else:
        formulario = RecetaForm()
    return render_to_response('recetaform.html', {'formulario': formulario},
                              context_instance=RequestContext(request))


def nuevoComentario(request):
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = ComentarioForm()
    return render_to_response('comentarioform.html', {'formulario': formulario},
                              context_instance=RequestContext(request))


def usuario(request):
    usuarios = User.objects.all()
    return render_to_response('usuario.html', {'usuarios': usuarios}, context_instance=RequestContext(request))


def usuarioNuevo(request):
    if request.method == 'POST':
        formulario = UserForm(request.POST, request.FILES)
        if formulario.is_valid():
            '''user = Usuario.objects.create(username=formulario.cleaned_data['username'],
                                          email=formulario.cleaned_data['email'],
                                          password=make_password(formulario.cleaned_data['password']),
                                          nombre=formulario.cleaned_data['nombre'])
            contenido = render_to_string('mailing/bienvenida.html', {'usuario': user,
                                                                     'pass': formulario.cleaned_data['password']})
            correo = EmailMessage('Bienvenido a SS', contenido,
                                  to=[formulario.cleaned_data['email']])
            correo.content_subtype = "html"
            correo.send()'''
            formulario.save()
            return HttpResponseRedirect('/usuario')
    else:
        formulario = UserForm()
    return render_to_response('usuarioform.html', {'formulario': formulario},
                              context_instance=RequestContext(request))


def recuperarPass(request):
    if request.method == 'POST':
        formulario = RecuperarPassForm(request.POST, request.FILES)
        if formulario.is_valid():
            password = generar_nuevo_pass(request, formulario.cleaned_data['correo'])
            contenido = render_to_string('mailing/recuperacion_password.html', {'pass': password})
            print str(contenido)
            correo = EmailMessage('Restablecimiento de Pass de SS', contenido,
                                  to=[formulario.cleaned_data['correo']])
            correo.content_subtype = "html"

            correo.send()
            return HttpResponseRedirect('/usuario')
    else:
        formulario = RecuperarPassForm()
    return render_to_response('recuperarpassform.html', {'formulario': formulario},
                              context_instance=RequestContext(request))


def generar_nuevo_pass(request, correo):
    if correo is not None:
        user = Usuario.objects.get(email=correo)
        password = ''.join([choice(string.letters + string.digits) for i in range(10)])
        user.password = make_password(password)
        user.save()
        return str(password)

    return None
