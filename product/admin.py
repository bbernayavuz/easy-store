from django.contrib import admin
from product.models import Category, Customer, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', "stock", "manufacturer")
    list_editable=('manufacturer',)
    search_fields= ("name",)
    readonly_fields= ("slug",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Customer)

