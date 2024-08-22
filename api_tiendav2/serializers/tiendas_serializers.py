from rest_framework import serializers

from ..models.tiendasModel import Tiendas

class TiendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiendas
        fields='__all__'