from django.urls import path
from . import views

app_name = 'jugadores'

urlpatterns = [
    path('', views.index, name='index'),
]