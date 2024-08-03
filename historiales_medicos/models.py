from django.db import models
from pacientes.models import Paciente

class HistorialMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Historial médico de {self.paciente}"
