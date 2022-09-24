from django.urls import include, path
from rest_framework.routers import DefaultRouter

from product.api import views as api_views

router = DefaultRouter()
router.register(r'product', api_views.ProductViewSet)
router.register(r'manufacturer', api_views.ManufacturerViewSet)
router.register(r'category', api_views.CategoryAPIView)


urlpatterns = [
    path('',include(router.urls)),
    # path("product/", api_views.ProductViewSet.as_view({'get':'list'}), name="product-list"),
    # path("product/<int:product_pk>", api_views.ProductViewSet.as_view({'get':'retrieve'}), name="product-detail"),
    # path("image/", api_views.ImageListCreateAPIView.as_view(), name="image-list"),
    path("product/<int:product_pk>/add_image", api_views.ProductImageCreateAPIView.as_view(), name="add-image"),
    # path("manufacturer/", api_views.ManufacturerListCreateAPIView.as_view(), name="manufacturer-list"),
    # path("manufacturer/<int:manufacturer_pk>", api_views.ManufacturerDetailAPIView.as_view(), name="manufacturer-detail"),
    # path("category/", api_views.CategoryListCreateAPIView.as_view(), name="category-list"),
    # path("category/<int:category_pk>", api_views.CategoryDetailAPIView.as_view(), name="category-detail"),
    path("product-category/", api_views.ProductCategoryListCreateAPIView.as_view(), name="product-category-list"),
    path("customer/", api_views.CustomerListCreateAPIView.as_view(), name="customer-list"),

]
