from rest_framework import permissions
from django.contrib.auth.models import User

class EsCliente(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff == 0:
            return True
        else:
            return False