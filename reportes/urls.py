# reportes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generar/', views.generar, name='generar'),
]
