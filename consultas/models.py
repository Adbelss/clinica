from django.db import models
from citas.models import Cita

class Consulta(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE)
    motivo = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"Consulta para la cita {self.cita.id}"
