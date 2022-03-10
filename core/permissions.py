from rest_framework.permissions import BasePermission

from core.models import BlockedIP


class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class BlocklistPermission(BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        ip_address = request.META["REMOTE_ADDR"]
        blocked = BlockedIP.objects.filter(ip_address=ip_address).exists()
        return not blocked
