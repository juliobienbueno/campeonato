from django.shortcuts import render
from .models import Jugador

# Create your views here.
def  lista_campeonato(request):
    return render(request,'campeonato/lista_campeonato.html',{})

