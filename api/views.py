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

class UsuarioUpdateAPIView(RetrieveUpdateAPIView):
    '''

    Edite um usuário 

    '''
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UsuarioDeleteAPIView(DestroyAPIView):
    '''

    Delete um usuário

    '''
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

############################ OCORRÊNCIA ##############################################

class OcorrenciaCreateAPIView(CreateAPIView):
    '''

    Crie uma nova ocorrência

    '''
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)       

class OcorrenciaDetailAPIView(RetrieveAPIView):
    '''

    Informações das ocorrências

    '''
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OcorrenciaListAPIView(ListAPIView):
    '''

    Liste as ocorrências

    '''
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OcorrenciaUpdateAPIView(RetrieveUpdateAPIView):
    '''

    Edite ocorrência

    '''
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OcorrenciaDeleteAPIView(DestroyAPIView):
    '''

    Delete uma ocorrência

    '''
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

############################ CATEGORIA ##############################################

class CategoriaCreateAPIView(CreateAPIView):
    '''

    Crie uma nova categoria

    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)       

class CategoriaDetailAPIView(RetrieveAPIView):
    '''

    Informações das categorias

    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CategoriaListAPIView(ListAPIView):
    '''

    Liste as categorias

    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CategoriaUpdateAPIView(RetrieveUpdateAPIView):
    '''

    Edite uma categoria

    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CategoriaDeleteAPIView(DestroyAPIView):
    '''

    Delete uma categoria

    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
