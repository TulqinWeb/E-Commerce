from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Customer GET qila oladi
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Admin CRUD qiladi
        return request.user.is_authenticated and request.user.role == "ADMIN"
