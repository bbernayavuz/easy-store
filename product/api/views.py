from rest_framework import viewsets

from product.api.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("name")
    serializer_class = ProductSerializer
