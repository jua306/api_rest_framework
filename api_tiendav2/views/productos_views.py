# En productos_views.py
from rest_framework import viewsets
from ..serializers import ProductoSerializer
from ..models.productosModel import Productos
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer
