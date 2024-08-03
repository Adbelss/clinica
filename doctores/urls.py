from django.urls import path
from . import views

urlpatterns = [
    path('registrar_doctor/', views.registrar_doctor, name='registrar_doctor'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
