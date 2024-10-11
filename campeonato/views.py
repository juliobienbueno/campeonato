from django.shortcuts import render

# Create your views here.
def  lista_campeonato(request):
    return render(request,'campeonato/lista_campeonato.html',{})
