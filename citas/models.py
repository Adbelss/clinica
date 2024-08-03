from django.db import models
from pacientes.models import Paciente
from doctores.models import Doctor

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField(max_length=1000)

    def __str__(self):
        return f"Cita con {self.doctor} el {self.fecha} a las {self.hora}"
