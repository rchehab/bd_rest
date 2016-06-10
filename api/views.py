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
from rest_framework import permissions
from django.contrib.auth.models import User, Group


#Adicionar resposta, descricao
#usuario feito no API nao consegue acessar o web
#criacao de usuario -> atualizar
#disparidades no BD
#Analisar campos ocorrencia
#permissoes
#autenticação

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