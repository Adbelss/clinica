from django.db import models

class Usuario(models.Model):
    DOCTOR = 'Doctor'
    EMPLEADO = 'Empleado'
    TIPO_USUARIO_CHOICES = [
        (DOCTOR, 'Doctor'),
        (EMPLEADO, 'Empleado'),
    ]
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)

    def __str__(self) -> str:
        return str(self.username)  # Forzar explícitamente el tipo de retorno a cadena
