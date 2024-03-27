from rest_framework.permissions import BasePermission


class IsOwnerForHabit(BasePermission):
    """Permission for owner for habit's views"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsOwnerForUser(BasePermission):
    """Permission for owner for user's views"""
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id
