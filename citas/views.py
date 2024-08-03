# citas/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a la página de citas")

def programar(request):
    return HttpResponse("Página de programación de citas")
