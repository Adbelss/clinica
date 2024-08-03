# empleados/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a la página de empleados")

def registro(request):
    return HttpResponse("Página de registro de empleados")
