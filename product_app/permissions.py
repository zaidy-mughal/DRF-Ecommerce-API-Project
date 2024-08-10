from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsOwnerOrReadOnly(BasePermission):
    """
    This is used to give object level permissions to only the user who are Owner can edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
    
    