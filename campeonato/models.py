from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Jugador(models.Model):
    nombre=models.CharField(max_length=400)
    equipo=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    direccion=models.CharField(max_length=400)
    fechaNacimiento=models.DateField