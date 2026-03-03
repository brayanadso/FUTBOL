from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    escudo = models.ImageField(upload_to='equipos/', blank=True, null=True)  # ← CAMBIADO
    director_tecnico = models.CharField(max_length=100)
    trofeos_ganados = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre