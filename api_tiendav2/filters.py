import django_filters
from .models.comprasModel import Compra

class CompraFilter(django_filters.FilterSet):
    cliente__nombre = django_filters.CharFilter(field_name='cliente__nombre', lookup_expr='icontains')
    tienda__nombre_tienda = django_filters.CharFilter(field_name='tienda__nombre_tienda', lookup_expr='icontains')
    producto__nombre_producto = django_filters.CharFilter(field_name='producto__nombre_producto', lookup_expr='icontains')
    # fecha = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Compra
        fields = ['cliente__nombre', 'tienda__nombre_tienda', 'producto__nombre_producto']
