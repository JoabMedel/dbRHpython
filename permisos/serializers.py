from rest_framework.serializers import ModelSerializer
from permisos.models import Permisos


class ShowPermisosSerializer(ModelSerializer):
    class Meta:
        model = Permisos
        fields = ('id', 'nombre_permiso')


class DetailPermisoSerializer(ModelSerializer):
    class Meta:
        model = Permisos
        fields = ('id', 'nombre_permiso', 'fecha_expedicion', 'fecha_expiracion', 'empleado')

