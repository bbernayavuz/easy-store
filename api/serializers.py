from itertools import product
from rest_framework import serializers

from product.models import Category, Manufacturer, Product, ProductImage, Customer
from order.models import Order, OrderItem

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
        # exclude = ["product"]
# 

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    # manufacturer = ManufacturerSerializer(read_only=True, many=False) #cevapta manufacturer serializerdaki tüm bilgileri verir.
    # manufacturer = serializers.StringRelatedField(read_only=False) # cevapta manufacturer name'ini verir.
                                                    # Manufacturer modelde dönen değeri verir  
                                                    # Ama product oluşturulurken yine manufacturer id verilmelidir.
    # manufacturer ile ilgili hiçbir şey yazılmazsa id döner.
    # category = CategorySerializer(many=True)

    image = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = "__all__"
        
 

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"



class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    orderitem_set=OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        # import pdb
        # pdb.set_trace()
        orderitem_validated_data = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        orderitem_set_serializer = self.fields['orderitem_set']
        for each in orderitem_validated_data:
            each['order'] = order
        orderitems = orderitem_set_serializer.create(orderitem_validated_data)

        return order

    # def get_items(self, obj):
    #     query = OrderItem.objects.filter(
    #         order_id=obj.id)
    #     serializer = OrderItemSerializer(query, many=True)

    #     return serializer.data