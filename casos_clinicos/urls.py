# casos_clinicos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('caso/', views.caso, name='caso'),
]
