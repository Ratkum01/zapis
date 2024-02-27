from rest_framework.permissions import BasePermission
from rest_framework import permissions
class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'client'

class IsMaster(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'master'

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and (request.user.is_staff or request.user.role == 'administrator'))