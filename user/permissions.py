from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request):
        return request.user.is_authenticated and request.user.is_admin
