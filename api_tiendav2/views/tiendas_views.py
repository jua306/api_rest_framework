from rest_framework import viewsets
from ..serializers import TiendasSerializer
from ..models.tiendasModel import Tiendas

class TiendasViewSet(viewsets.ModelViewSet):
    queryset= Tiendas.objects.all()
    serializer_class =TiendasSerializer