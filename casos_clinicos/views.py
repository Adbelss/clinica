# casos_clinicos/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a la página de casos clínicos")

def caso(request):
    return HttpResponse("Página de casos clínicos")
