from rest_framework import generics
from permisos.models import Permisos
from permisos.serializers import ShowPermisosSerializer, DetailPermisoSerializer


class PermisosViews(generics.ListCreateAPIView):
    queryset = Permisos.objects.all()
    serializer_class = ShowPermisosSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return DetailPermisoSerializer
        return ShowPermisosSerializer


class PermisoDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permisos.objects.all()
    serializer_class = DetailPermisoSerializer



