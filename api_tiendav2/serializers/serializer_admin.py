from rest_framework import serializers
from ..models.clientesModel import Clientes
from ..models.productosModel import Productos
from ..models.tiendasModel import Tiendas
from ..models.comprasModel import Compra
from ..serializers.clientes_serializers import ClientesSerializers
from ..serializers.productos_serializers import ProductoSerializer
from ..serializers.tiendas_serializers import TiendasSerializer

class CompraCompleteSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Clientes.objects.all(), required=False)
    tienda = serializers.PrimaryKeyRelatedField(queryset=Tiendas.objects.all(), required=False)
    producto = serializers.PrimaryKeyRelatedField(queryset=Productos.objects.all(), required=False)

    cliente_detail = ClientesSerializers(source='cliente', read_only=True)
    tienda_detail = TiendasSerializer(source='tienda', read_only=True)  # Corregido aquí
    producto_detail = ProductoSerializer(source='producto', read_only=True)  # Corregido aquí

    class Meta:
        model = Compra
        fields = '__all__'
        extra_kwargs = {
            'cliente': {'required': False},
            'tienda': {'required': False},
            'producto': {'required': False},
        }
