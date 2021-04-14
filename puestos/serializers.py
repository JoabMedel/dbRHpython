from rest_framework.serializers import ModelSerializer
from puestos.models import Puestos


class PuestosSerializer(ModelSerializer):
    class Meta:
        model = Puestos
        fields = ('id', 'nombre')
