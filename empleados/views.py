from rest_framework.viewsets import ModelViewSet
from empleados.models import Empleados
from empleados.serializers import ShowEmpleadosSerializer, DetailEmpleadoSerializer, AddNewEmpleadoSerializer


class EmpleadosViewSet(ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = ShowEmpleadosSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'retrieve':
            return DetailEmpleadoSerializer
        if self.action == 'create':
            return AddNewEmpleadoSerializer
        return ShowEmpleadosSerializer
