from django.db import models
from usuarios.models import Usuario

class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    fecha = models.DateField()

    def __str__(self):
        return f"Notificación para {self.usuario} el {self.fecha}"
