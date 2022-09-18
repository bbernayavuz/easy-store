from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from product.enums import Gender

# from django.utils.timezone import datetime



class Manufacturer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120)
    # created_at = models.DateTimeField(default=datetime.now())
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
    category = models.ManyToManyField(Category, through="ProductCategory")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class ProductCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductImage(models.Model):
    image_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_id



class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255, choices=Gender.choices())

    # def __str__(self):
    #     return self.username

