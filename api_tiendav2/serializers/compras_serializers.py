from rest_framework import serializers
from ..models.comprasModel import Compra


class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields ='__all__'