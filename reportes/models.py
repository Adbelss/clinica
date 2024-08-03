from django.db import models
from usuarios.models import Usuario

class Reporte(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=45)
    contenido = models.TextField()
    fecha_generacion = models.DateField()

    def __str__(self):
        return f"Reporte generado por {self.usuario} el {self.fecha_generacion}"
