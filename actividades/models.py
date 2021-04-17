from django.db import models
from empleados.models import Empleados


class Actividades(models.Model):
    nombre = models.CharField(max_length=200)
    empleados = models.ManyToManyField(
        Empleados,
        related_name='Actividades',
    )

    def __str__(self):
        return self.nombre
