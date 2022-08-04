from django.urls import include, path
from rest_framework import routers

from product.api import views as api_views

urlpatterns = [
    path("product/", api_views.ProductListCreateAPIView.as_view(), name="product-list"),
    path("image/", api_views.ImageListCreateAPIView.as_view(), name="image-list"),
    path("product/<int:product_pk>", api_views.ProductDetailAPIView.as_view(), name="product-detail"),
    path("product/<int:product_pk>/add_image", api_views.ProductImageCreateAPIView.as_view(), name="add-image"),
    path("manufacturer/", api_views.ManufacturerListCreateAPIView.as_view(), name="manufacturer-list"),
    path("category/", api_views.CategoryListCreateAPIView.as_view(), name="category-list"),
    path("product-category/", api_views.ProductCategoryListCreateAPIView.as_view(), name="product-category-list"),
]


# routers = routers.DefaultRouter()
# routers.register("", views.ProductViewSet)

# urlpatterns = [
#     path("", include(routers.urls)),
#     path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
# ]
