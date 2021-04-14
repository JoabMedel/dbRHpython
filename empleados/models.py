from django.db import models

from puestos.models import Puestos


class Empleados(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    puesto = models.ForeignKey(
        Puestos,
        related_name='Puesto',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nombre
