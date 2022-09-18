from rest_framework import generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import permissions
from product.api.permissions import IsAdminUserOrReadOnly

from product.api.serializers import (
    CategorySerializer,
    ImageSerializer,
    ManufacturerSerializer,
    ProductCategorySerializer,
    ProductImageSerializer,
    ProductSerializer,
    ProfileSerializer,
)
from product.models import Category, Manufacturer, Product, ProductCategory, ProductImage, Profile

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)




class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ImageSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "product_pk"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageCreateAPIView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def perform_create(self, serializer):
        product_pk = self.kwargs.get("product_pk")
        product = get_object_or_404(Product, pk=product_pk)
        serializer.save(product=product)


class ManufacturerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes =  [IsAdminUserOrReadOnly]



# 1
# class ProductViewSet(viewsets.ModelViewSet):
#      queryset = Product.objects.all().order_by("name")
#      serializer_class = ProductSerializer


# class ProductListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
