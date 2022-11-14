from rest_framework.permissions import BasePermission


class IsBrandUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.Role.Brand)


class IsInfluencerUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.Role.Influencer)


class IsEmployeeUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.Role.Employee)