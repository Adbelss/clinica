from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import Group  # Asegúrate de importar Group
from .forms import RegistroForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'usuarios/login.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

# Verificación de si el usuario es doctor
def es_doctor(user):
    return user.groups.filter(name='Doctores').exists()

# Vista del dashboard del doctor
@login_required
@user_passes_test(es_doctor)
def doctor_dashboard(request):
    return render(request, 'usuarios/doctor_dashboard.html')

# Vista para registrar un doctor
@login_required
def registrar_doctor(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asegúrate de que el grupo "Doctores" existe
            doctor_group, created = Group.objects.get_or_create(name='Doctores')
            user.groups.add(doctor_group)
            user.save()
            return redirect('doctor_dashboard')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registrar_doctor.html', {'form': form})

