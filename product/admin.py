from django.contrib import admin
from product.models import Category, Product, Profile



# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Profile)

