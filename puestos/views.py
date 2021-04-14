from rest_framework import generics
from puestos.models import Puestos
from puestos.serializers import PuestosSerializer


class PuestosViews(generics.ListCreateAPIView):
    queryset = Puestos.objects.all()
    serializer_class = PuestosSerializer


class PuestoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Puestos.objects.all()
    serializer_class = PuestosSerializer
