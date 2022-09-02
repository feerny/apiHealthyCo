from rest_framework import serializers
from healthyapp.models import Producto


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields =(
            "id",
            "nombre",
            "price",
            "descripcion",
            "imagen"
        )