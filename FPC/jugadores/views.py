from django.shortcuts import render, get_object_or_404
from .models import Jugador

def index(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadores/index.html', {'jugadores': jugadores})

def detalle(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    historial = jugador.historial.all()
    return render(request, 'jugadores/detalle.html', {
        'jugador': jugador,
        'historial': historial,
    })