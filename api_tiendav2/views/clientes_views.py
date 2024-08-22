from rest_framework import viewsets
from ..serializers import ClientesSerializers
from ..models.clientesModel import Clientes

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class =ClientesSerializers
    