from urllib.request import Request
from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin=super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin

# bir profil eklendiğinde user'ın sadece kendi profilini görmesini sağlar.
class IsOwnUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user