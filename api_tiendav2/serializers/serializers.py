from rest_framework import serializers
from ..models.comprasModel import Compra

class CompraBasicSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    tienda_nombre = serializers.CharField(source='tienda.nombre_tienda', read_only=True)
    producto_nombre = serializers.CharField(source='producto.nombre_producto', read_only=True)

    class Meta:
        model = Compra
        fields = ['id', 'fecha', 'cliente_nombre', 'tienda_nombre', 'producto_nombre']
