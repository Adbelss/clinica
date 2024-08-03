# citas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programar/', views.programar, name='programar'),
]
