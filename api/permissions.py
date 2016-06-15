# -*- coding: utf-8 -*- 
from rest_framework import permissions
from django.contrib.auth.models import Group
from usuario.models import Usuario

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
        
class DonoOuVigilanteOuAdminPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
            usuario = Usuario.objects.get(pk=obj.usuario_ID)
            
            if usuario.user.groups.filter(id=1).exists():
                
                # Write permissions are only allowed to the owner of the snippet
                return usuario.user == request.user
            else:
                return True

class VigilanteOuAdminPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
            
            if request.user.groups.filter(id=1).exists():
                # Write permissions are only allowed to the owner of the snippet
                return False
            else:
				return True