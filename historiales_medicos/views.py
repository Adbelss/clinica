# historiales_medicos/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a la página de historiales médicos")

def historial(request):
    return HttpResponse("Página de historial médico")
