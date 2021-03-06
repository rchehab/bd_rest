# -*- coding: utf-8 -*- 
from rest_framework import permissions
from django.contrib.auth.models import Group
from usuario.models import Usuario

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
