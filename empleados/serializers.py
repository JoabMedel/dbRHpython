from rest_framework.serializers import ModelSerializer
from empleados.models import Empleados


class ShowEmpleadosSerializer(ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('id', 'nombre')


class DetailEmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('id', 'nombre', 'apellido', 'edad', 'puesto')

