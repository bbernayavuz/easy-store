from django.urls import path

from product.views import *

app_name = "product"

urlpatterns = [
    path("list/", product_list, name="product_list"),
    path("create/", product_create, name="product_create"),
    path("update/<int:id>", product_update, name="product_update"),
    path("delete/<int:id>", product_delete, name="product_delete"),
]
