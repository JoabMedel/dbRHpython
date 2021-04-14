from django.db import models
from empleados.models import Empleados


class Permisos(models.Model):
    nombre_permiso = models.CharField(max_length=200)
    fecha_expedicion = models.DateField()
    fecha_expiracion = models.DateField()
    empleado = models.ForeignKey(
        Empleados,
        related_name='empleado',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nombre_permiso

