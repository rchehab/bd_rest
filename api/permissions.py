# -*- coding: utf-8 -*- 
from rest_framework import permissions
from django.contrib.auth.models import Group
from usuario.models import Usuario


class DonoOuVigilanteOuAdminPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
            print(obj.usuario_ID)
            usuario = Usuario.objects.get(pk=obj.usuario_ID)
            print(usuario.user.groups.all())
            
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
            
            print(request.user)
            print(request.user.groups.all())
            
            if request.user.groups.filter(id=1).exists():
                print(1)
                # Write permissions are only allowed to the owner of the snippet
                return False
            else:
                print(0)
                return True
