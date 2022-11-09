from rest_framework import generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import permissions
from api.permissions import IsAdminUserOrReadOnly, IsOwnUserOrReadOnly
from rest_framework import status
from rest_framework.response import Response

from api.serializers import (
    CategorySerializer,
    ImageSerializer,
    ManufacturerSerializer,
    ProductImageSerializer,
    ProductSerializer,
    CustomerSerializer,
    OrderSerializer,
)
from product.models import Category, Customer, Manufacturer, Product, ProductImage, Customer
from order.models import Order,OrderItem

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from rest_framework.filters import SearchFilter



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
    filter_backends=[SearchFilter] # birden fazla seçenek eklenebilir
    search_fields=['name'] #product modelinden birden fazla seçenek eklenebilir

 
    def retrieve(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



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


class CategoryViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.ListModelMixin,
                                GenericViewSet):
    lookup_url_kwarg = "category_pk"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


# class ProductCategoryListCreateAPIView(generics.ListCreateAPIView):
#     queryset = ProductCategory.objects.all()
#     serializer_class = ProductCategorySerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)


class CustomerViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
                            
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =  [IsAdminUserOrReadOnly,]

    def get_queryset(self):
        queryset = Customer.objects.all()
        username= self.request.query_params.get('username', None)
        if username is not None:
            queryset=queryset.filter(user__username=username)
        return queryset



class OrderViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):

    lookup_url_kwarg = "order_pk"
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[SearchFilter] # birden fazla seçenek eklenebilir


    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

