from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('partidos',views.partidos, name='partidos'),
    path('partido',views.partido, name='partido'),
    path('equipos',views.equipos, name='equipos'),
    path('campeonatos',views.campeonatos, name='campeonatos'),
    path('sesioniniciada',views.sesioniniciada, name='sesioniniciada'),
    path('digitarPartido',views.digitarPartido, name='digitarPartido'),
    
]   