# historiales_medicos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('historial/', views.historial, name='historial'),
]
