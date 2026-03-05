from django.urls import path
from . import views

app_name = 'equipos'

urlpatterns = [
    path ('', views.equipo, name='equipo'),
    path('<int:id>/', views.detalle, name='detalle'),
]


