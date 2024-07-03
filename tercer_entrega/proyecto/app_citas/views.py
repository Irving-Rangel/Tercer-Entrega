from django.shortcuts import render
from .models import *

# Create Irving Rangel.

def home(request):
    return render(request, "app_citas/index.html")

def departamento(request):
    contexto = {"departamentos": Departamento.objects.all()}
    return render(request, "app_citas/#departamento", contexto)