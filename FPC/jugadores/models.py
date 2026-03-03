from django.db import models
from equipos.models import Equipo
from django.utils import timezone

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    numero_camiseta = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')
    foto = models.ImageField(upload_to='jugadores/', blank=True, null=True)
    # Nuevos campos
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=100, blank=True)
    altura = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, help_text="Metros, ej: 1.80")
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Kg, ej: 75.5")
    goles_totales = models.IntegerField(default=0)

    def edad(self):
        if self.fecha_nacimiento:
            hoy = timezone.now().date()
            return hoy.year - self.fecha_nacimiento.year - (
                (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
            )
        return None

    def __str__(self):
        return self.nombre


class HistorialClub(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='historial')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='historial_jugadores')
    goles = models.IntegerField(default=0)
    temporadas = models.CharField(max_length=50, help_text="Ej: 2020-2022")

    def __str__(self):
        return f"{self.jugador.nombre} - {self.equipo.nombre}"