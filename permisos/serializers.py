from rest_framework.serializers import ModelSerializer
from empleados.serializers import DetailEmpleadoSerializer
from permisos.models import Permisos


class ShowPermisosSerializer(ModelSerializer):
    class Meta:
        model = Permisos
        fields = ('id', 'nombre_permiso')


class DetailPermisoSerializer(ModelSerializer):
    empleado = DetailEmpleadoSerializer()

    class Meta:
        model = Permisos
        fields = ('id', 'nombre_permiso', 'fecha_expedicion', 'fecha_expiracion', 'empleado')


class AddNewPermisoSerializer(ModelSerializer):
    class Meta:
        model = Permisos
        fields = ('id', 'nombre_permiso', 'fecha_expedicion', 'fecha_expiracion', 'empleado')