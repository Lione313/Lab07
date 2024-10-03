
from django.shortcuts import render, redirect
from .models import Evento, RegistroEvento, Usuario
from .forms import EventoForm, RegistroEventoForm

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)  
        if form.is_valid():
            evento = form.save() 
            return redirect('eventos') 
    else:
        form = EventoForm() 

    return render(request, 'crear_evento.html', {'form': form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos')  
    else:
        form = RegistroEventoForm()
    return render(request, 'registrar_usuario.html', {'form': form})


def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listar_eventos.html', {'eventos': eventos})
