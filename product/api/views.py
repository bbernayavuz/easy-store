from rest_framework import generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import permissions
from product.api.permissions import IsAdminUserOrReadOnly, IsOwnUserOrReadOnly

from product.api.serializers import (
    CategorySerializer,
    ImageSerializer,
    ManufacturerSerializer,
    ProductCategorySerializer,
    ProductImageSerializer,
    ProductSerializer,
    CustomerSerializer,
)
from product.models import Category, Customer, Manufacturer, Product, ProductCategory, ProductImage, Customer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins



class ProductViewSet(
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):

    lookup_url_kwarg = "product_pk"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProductImageCreateAPIView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        product_pk = self.kwargs.get("product_pk")
        product = get_object_or_404(Product, pk=product_pk)
        serializer.save(product=product)


class ManufacturerViewSet(ModelViewSet):
    lookup_url_kwarg = "manufacturer_pk"
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CategoryAPIView(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.ListModelMixin,
                                GenericViewSet):
    lookup_url_kwarg = "category_pk"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProductCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =  [IsAdminUserOrReadOnly,]

