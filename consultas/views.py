# consultas/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a la página de consultas")

def detalles(request):
    return HttpResponse("Página de detalles de consultas")
