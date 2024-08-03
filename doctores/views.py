from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from .forms import DoctorRegistrationForm

# Verificación de si el usuario es doctor
def es_doctor(user):
    return user.groups.filter(name='Doctores').exists()

# Vista del dashboard del doctor
@login_required
@user_passes_test(es_doctor)
def doctor_dashboard(request):
    return render(request, 'doctores/doctor_dashboard.html')

# Vista para registrar un doctor
@login_required
def registrar_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            doctor_group, created = Group.objects.get_or_create(name='Doctores')
            user.groups.add(doctor_group)
            user.save()
            return redirect('doctor_dashboard')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctores/registrar_doctor.html', {'form': form})
