from rest_framework import serializers

from product.models import Category, Manufacturer, Product, ProductCategory, ProductImage, Customer

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
    manufacturer = serializers.StringRelatedField() # cevapta manufacturer name'ini verir.
                                                    # Manufacturer modelde dönen değeri verir  
                                                    # Ama product oluşturulurken yine manufacturer id verilmelidir.
    # manufacturer ile ilgili hiçbir şey yazılmazsa id döner.
    category = CategorySerializer(read_only=True, many=True)
    image = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"