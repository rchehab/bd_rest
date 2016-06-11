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
from api.password import password

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#Adicionar resposta, descricao
#usuario feito no API nao consegue acessar o web
#criacao de usuario -> atualizar
#disparidades no BD
#Analisar campos ocorrencia
#permissoes
#autenticação

############################ USER ##############################################

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
class UsuarioList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        u = User.objects.create(username=request.data['login'],
            email = request.data['email'])

        u.set_password(request.data['senha'])
        request.data['user'] = u.id

        hashed_password = password.hash_this(request.data['senha'])
        
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['senha'] = hashed_password

        if serializer.is_valid():
            u.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        
        if serializer.is_valid():
            if request.data['login'] != usuario.login or request.data['email'] != usuario.email or request.data['senha'] != usuario.senha:
                user = User.objects.get(pk=usuario.user.pk)
                user.username = request.data['login']
                user.email = request.data['email']
                user.set_password(request.data['senha'])
                user.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        u = User.objects.get(id = serializer.data['user'])
        u.delete()
        usuario.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)

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
