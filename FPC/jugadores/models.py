from django.db import models
from equipos.models import Equipo

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    numero_camiseta = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')
    foto = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre