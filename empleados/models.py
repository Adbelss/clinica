from django.db import models
from usuarios.models import Usuario

class Empleado(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=45)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
