from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from puestos.models import Puestos
from puestos.serializers import PuestosSerializer


class PuestoViewSet(ModelViewSet):
    queryset = Puestos.objects.all()
    serializer_class = PuestosSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # def get_queryset(self):
    #     nombre = self.request.query_params.get('nombre')
    #     datos = self.queryset.filter(nombre=nombre)
    #     return datos

