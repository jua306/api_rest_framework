from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.comprasModel  import Compra
from ..serializers.serializers import CompraBasicSerializer
from ..serializers.serializer_admin import CompraCompleteSerializer
from ..filters import CompraFilter
from django_filters.rest_framework import DjangoFilterBackend

class CompraView(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompraFilter

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return CompraCompleteSerializer
        return CompraBasicSerializer

