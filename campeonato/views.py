from django.shortcuts import render
from django.http import JsonResponse
from .supabase_client import supabase  # Importa el cliente de Supabase
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def inicio(request):
    return render(request,'campeonato/inicio.html')

def partidos(request):
    return render(request,'campeonato/partidos.html')

def partido(request):
    return render(request,'campeonato/partido.html')

def equipos(request):
    return render(request,'campeonato/equipos.html')

def campeonatos(request):
    return render(request,'campeonato/campeonatos.html')

def digitarPartido(request):
    return render(request,'campeonato/digitarPartido.html')

@csrf_exempt  # Permite solicitudes POST desde JavaScript
def sesioniniciada(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Intento de autenticación con Supabase
        try:
            response = supabase.auth.sign_in_with_password(email=email, password=password)
            if response.user:
                # Si la autenticación es exitosa, guarda el ID del usuario en la sesión de Django
                request.session["idUsuario"] = response.user.id
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "error": "Credenciales inválidas"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Petición inválida"})


def logout_view(request):
    request.session.flush()  # Elimina la sesión del usuario
    return JsonResponse({"success": True})
