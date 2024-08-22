from  rest_framework import serializers
from ..models.clientesModel import Clientes



class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields= '__all__'
