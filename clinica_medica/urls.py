from django.contrib import admin
from django.urls import path, include
from . import views  # Importar las vistas del proyecto principal
from django.contrib.auth import views as auth_views  # Importar auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('usuarios/', include('usuarios.urls')),
    path('doctores/', include('doctores.urls')),
    path('empleados/', include('empleados.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('citas/', include('citas.urls')),
    path('consultas/', include('consultas.urls')),
    path('historiales_medicos/', include('historiales_medicos.urls')),
    path('casos_clinicos/', include('casos_clinicos.urls')),
    path('tratamientos/', include('tratamientos.urls')),
    path('notificaciones/', include('notificaciones.urls')),
    path('reportes/', include('reportes.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
