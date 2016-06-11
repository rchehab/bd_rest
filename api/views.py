# -*- coding: utf-8 -*- 
from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from usuario.models import Usuario
from ocorrencia.models import Categoria, Ocorrencia
from api.serializers import UsuarioSerializer, OcorrenciaSerializer, CategoriaSerializer, UserSerializer, GroupSerializer
from rest_framework import permissions, status
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view
from rest_framework.response import Response


#Adicionar resposta, descricao
#usuario feito no API nao consegue acessar o web
#criacao de usuario -> atualizar
#disparidades no BD
#Analisar campos ocorrencia
#permissoes
#autenticação
############################# REQUESTS #########################################
# @api_view(['GET', 'PUT', 'DELETE'])
#def snippet_detail(request, pk):
#    """
#    Retrieve, update or delete a snippet instance.
#    """
#    try:
#        snippet = Snippet.objects.get(pk=pk)
#    except Snippet.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#   if request.method == 'GET':
#       serializer = SnippetSerializer(snippet)
#       return Response(serializer.data)

#   elif request.method == 'PUT':
#       serializer = SnippetSerializer(snippet, data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#
#   elif request.method == 'DELETE':
#
#
#
#       snippet.delete()
 #
#
#
#       return Response(status=status.HTTP_204_NO_CONTENT)
############################ USER ##############################################
class UserCreateAPIView(CreateAPIView):
    '''
    
    Crie um novo user
    
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(RetrieveAPIView):
    '''
    
    Detalhes dos user
    
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    '''

    Lista dos user

    '''
class UserListAPIView(ListAPIView):
    '''
    
    Lista dos user
    
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserUpdateAPIView(RetrieveUpdateAPIView):
    '''
    
    Edite um user 
    
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserDeleteAPIView(DestroyAPIView):
    '''
    
    Delete um user
    
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

############################ GROUP ##############################################
class GroupDetailAPIView(RetrieveAPIView):
    '''
    
    Detalhes dos grupos de usuários
    
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GroupListAPIView(ListAPIView):
    '''
    
    Lista dos grupos
    
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

############################ USUÁRIO ##############################################
class UsuarioCreateAPIView(CreateAPIView):
    '''
    
    Crie um novo usuário
    
    '''
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailAPIView(RetrieveAPIView):
    '''
    
    Detalhes dos usuários
    
    '''
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UsuarioListAPIView(ListAPIView):
    '''
    
    Lista dos usuários
    
    '''
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    '''

    Edite um usuário 

    '''
class UsuarioUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    '''

    Delete um usuário

    '''
class UsuarioDeleteAPIView(DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

############################ OCORRÊNCIA ##############################################
    '''

    Crie uma nova ocorrência

    '''
class OcorrenciaCreateAPIView(CreateAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)       

    '''

    Informações das ocorrências

    '''
class OcorrenciaDetailAPIView(RetrieveAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    '''

    Liste as ocorrências

    '''
class OcorrenciaListAPIView(ListAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    '''

    Edite ocorrência

    '''
class OcorrenciaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    '''

    Delete uma ocorrência

    '''
class OcorrenciaDeleteAPIView(DestroyAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

############################ CATEGORIA ##############################################

    '''

    Crie uma nova categoria

    '''
class CategoriaCreateAPIView(CreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)       

    '''

    Informações das categorias

    '''
class CategoriaDetailAPIView(RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    '''

    Liste as categorias

    '''
class CategoriaListAPIView(ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    '''

    Edite uma categoria

    '''
class CategoriaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    '''

    Delete uma categoria

    '''
class CategoriaDeleteAPIView(DestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)