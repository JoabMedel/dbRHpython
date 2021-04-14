from rest_framework import generics
from empleados.models import Empleados
from empleados.serializers import ShowEmpleadosSerializer, DetailEmpleadoSerializer


class EmpleadosViews(generics.ListCreateAPIView):
    queryset = Empleados.objects.all()
    serializer_class = ShowEmpleadosSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return DetailEmpleadoSerializer
        return ShowEmpleadosSerializer


class EmpleadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleados.objects.all()
    serializer_class = DetailEmpleadoSerializer

