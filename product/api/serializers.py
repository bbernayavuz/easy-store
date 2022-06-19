from pyexpat import model
from rest_framework import serializers

from product.models import Manufacturer, Product


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"s


class ProductSerializer(serializers.ModelSerializer):
    manufacturers = ManufacturerSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = "__all__"



