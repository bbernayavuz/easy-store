from django.urls import include, path
from rest_framework import routers

from product.api import views

routers = routers.DefaultRouter()
routers.register("", views.ProductViewSet)

urlpatterns = [
    path("", include(routers.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
