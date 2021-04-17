from rest_framework.viewsets import ModelViewSet
from permisos.models import Permisos
from permisos.serializers import ShowPermisosSerializer, DetailPermisoSerializer, AddNewPermisoSerializer


class PermisosViewSet(ModelViewSet):
    queryset = Permisos.objects.all()
    serializer_class = ShowPermisosSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "create":
            return AddNewPermisoSerializer
        if self.action == "retrieve":
            return DetailPermisoSerializer
        return ShowPermisosSerializer




