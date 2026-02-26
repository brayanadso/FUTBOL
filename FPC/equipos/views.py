
from django.shortcuts import render, get_object_or_404
from .models import Equipo

def home(request):
    return render(request, 'equipos/home.html')

def index(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/index.html', {'equipos': equipos})

def detalle(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    jugadores = equipo.jugadores.all()
    return render(request, 'equipos/detalle.html', {'equipo': equipo, 'jugadores': jugadores})