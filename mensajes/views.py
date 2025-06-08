from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def bandeja_entrada(request):
    mensajes = request.user.mensajes_recibidos.all()
    return render(request, 'mensajes/bandeja.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST, user=request.user)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('bandeja')
    else:
        form = MensajeForm(user=request.user)
    return render(request, 'mensajes/enviar.html', {'form': form})

@login_required
def ver_mensaje(request, mensaje_id):
    mensaje = Mensaje.objects.get(id=mensaje_id, receptor=request.user)
    mensaje.leido = True
    mensaje.save()

    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            Mensaje.objects.create(
                emisor=request.user,
                receptor=mensaje.emisor,
                contenido=contenido
            )
            return redirect('bandeja')

    return render(request, 'mensajes/ver_mensaje.html', {'mensaje': mensaje})

@login_required
def responder_rapido(request, mensaje_id):
    if request.method == 'POST':
        if not request.user.is_staff and not request.user.is_superuser:
            return HttpResponseForbidden("No tienes permisos para responder directamente.")

        mensaje_original = get_object_or_404(Mensaje, id=mensaje_id)
        contenido = request.POST.get('contenido')

        if contenido:
            Mensaje.objects.create(
                emisor=request.user,
                receptor=mensaje_original.emisor,
                contenido=contenido
            )
            messages.success(request, "Respuesta enviada correctamente.")
        else:
            messages.warning(request, "No se puede enviar un mensaje vacío.")

        return redirect('bandeja')
