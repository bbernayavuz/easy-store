from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from product.enums import Gender, UserType
from phonenumber_field.modelfields import PhoneNumberField
import itertools

# from django.utils.timezone import datetime



class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, unique=True, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Manufacturer, self).save( *args, **kwargs)



class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, unique=True, editable=False, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True)
    category = models.ManyToManyField("Category")
    image = models.ManyToManyField("ProductImage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.pk:
            slug = slugify(self.name)

            for n in itertools.count(1):
                if not Product.objects.filter(slug=slug).exists():
                    self.slug = slug
                    break
                slug = '{}-{}'.format(slugify(self.name), n + 1);
        return super(Product, self).save( *args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, unique=True, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save( *args, **kwargs)


class ProductImage(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255, choices=Gender.choices(),null=False, blank=True)
    phone_number = PhoneNumberField(null=True)
    user_type = models.CharField(max_length=255,choices=UserType.choices(), blank=True)

    def __str__(self):
        return self.user.username
