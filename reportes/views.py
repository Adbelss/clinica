# reportes/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a la página de reportes")

def generar(request):
    return HttpResponse("Página de generar reportes")
