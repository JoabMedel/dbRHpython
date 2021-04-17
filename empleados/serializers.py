from rest_framework.serializers import ModelSerializer
from empleados.models import Empleados
from puestos.serializers import PuestosSerializer


class ShowEmpleadosSerializer(ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('id', 'nombre', 'puesto')


class DetailEmpleadoSerializer(ModelSerializer):
    puesto = PuestosSerializer()

    class Meta:
        model = Empleados
        fields = ('id', 'nombre', 'apellido', 'edad', 'puesto')


class AddNewEmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('id', 'nombre', 'apellido', 'edad', 'puesto')
