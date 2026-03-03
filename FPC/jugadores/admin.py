from django.contrib import admin
from .models import Jugador, HistorialClub

class HistorialClubInline(admin.TabularInline):
    model = HistorialClub
    extra = 1  # Muestra 1 fila vacía para agregar

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    inlines = [HistorialClubInline]

@admin.register(HistorialClub)
class HistorialClubAdmin(admin.ModelAdmin):
    list_display = ['jugador', 'equipo', 'temporadas', 'goles']