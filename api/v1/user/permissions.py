from rest_framework import permissions


class ProjectPermission(permissions.BasePermission):
    """Права для проекта."""

    def has_permission(self, request, view):
        return (
                request.method in ('GET', 'PUT', 'DELETE')
                or (request.user.is_staff and request.user.is_superuser)
        )

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to access the object.

        Args:
            request (HttpRequest): The request object.
            view (View): The view object.
            obj (Object): The object being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        # Check if the request method is safe (e.g., GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the object is the user's own object
        if obj == request.user:
            return True

        # Check if the user is a staff member
        if request.user.is_staff:
            return True

        return False