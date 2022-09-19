from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from product.enums import Gender, UserType
from phonenumber_field.modelfields import PhoneNumberField


# from django.utils.timezone import datetime



class Manufacturer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True)
    category = models.ManyToManyField("Category", through="ProductCategory")
    image = models.ManyToManyField("ProductImage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120)
    # created_at = models.DateTimeField(default=datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name



class ProductCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductImage(models.Model):
    image_id = models.BigAutoField(primary_key=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_id



class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255, choices=Gender.choices(),null=False, blank=True)
    phone_number = PhoneNumberField(null=True)
    user_type = models.CharField(max_length=255,choices=UserType.choices(), blank=True)

    def __str__(self):
        return self.username
