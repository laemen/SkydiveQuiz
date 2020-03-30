from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS

class IsAdminOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class IsAuthorOrReadOnly(BasePermission):

    def has_object(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

