from django.db import models
from pacientes.models import Paciente
from doctores.models import Doctor

class CasoClinico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=1000)
    fecha = models.DateField()

    def __str__(self):
        return f"Caso clínico de {self.paciente} atendido por {self.doctor}"
