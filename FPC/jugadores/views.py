from django.shortcuts import render
from .models import Jugador
# Create your views here.

def index(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadores/index.html', {'jugadores': jugadores})



