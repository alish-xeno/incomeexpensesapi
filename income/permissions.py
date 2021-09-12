from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsCustomer(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.groups.first().name == 'Customer') and request.user.is_active and request.user.is_verified
