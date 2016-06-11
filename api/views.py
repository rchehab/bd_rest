# -*- coding: utf-8 -*- 
# VIEWS DA API - UNB ALERTA - REST FRAMEWORK 


# Importando generics da rest framework para a criação da APIView
from rest_framework.generics import (
    
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView

    ) 

from rest_framework.views import APIView

# Importando os models preestabelecidos pelo Django e os models do UnB Alerta
from django.contrib.auth.models import User, Group
from usuario.models import Usuario
from ocorrencia.models import Categoria, Ocorrencia

# Importando os serializers de cada classe usada
from api.serializers import (

    UsuarioSerializer, 
    OcorrenciaSerializer, 
    CategoriaSerializer, 
    UserSerializer, 
    GroupSerializer

    )

# Importando arquivo com as permissões de User 
from rest_framework import permissions

# Importando classe password, utilizada para o hashing da senha
from api.password import password

# Outros imports 
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


############################ USER ##############################################
# Listagem de Users internos do Django bem quanto seus detalhes.
class UserDetailAPIView(RetrieveAPIView):
    '''
    
    Detalhes dos users
    
    '''
    queryset = User.objects.all() # Retorna todos os User
    serializer_class = UserSerializer # Utiliza a classe serializer User
    permission_classes = (permissions.IsAuthenticated,) 

class UserListAPIView(ListAPIView):
    '''
    
    Lista dos users
    
    '''
    queryset = User.objects.all() # Retorna todos os User
    serializer_class = UserSerializer # Utiliza a classe serializer User
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

############################ GROUP ##############################################
# Listagem de Groups internos do Django bem quanto seus detalhes.
class GroupDetailAPIView(RetrieveAPIView):
    '''
    
    Detalhes dos grupos de users
    
    '''
    queryset = Group.objects.all() # Retorna todos os Groups
    serializer_class = GroupSerializer # Utiliza a classe serializer Group
    permission_classes = (permissions.IsAuthenticated,)


class GroupListAPIView(ListAPIView):
    '''
    
    Lista dos grupos de users
    
    '''
    queryset = Group.objects.all() # Retorna todos os Groups
    serializer_class = GroupSerializer # Utiliza a classe serializer Group
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

############################ USUÁRIO ##############################################
# Listagem de Usuários do UnB Alerta com funções adicionais

class UsuarioList(APIView):
    """

    Lista todos os usuários e permite a criação.

    """
    # Função get: Retorna todos os usuários do banco
    def get(self, request, format = None):

        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many = True)
        return Response(serializer.data)

    # Função post: Cria um novo usuário 
    def post(self, request, format = None):
        # A partir das informações fornecidas precisamos criar um user
        # Um user interno do Django segue os padroes do Django de autenticação
        u = User.objects.create(
                username = request.data['login'], # Passamos o login
                email = request.data['email'] # Passamos o email
            )

        # Utilizando a encryption do Django podemos usar a função
        # set_password para passar a senha utilizada para o registro
        u.set_password(request.data['senha'])

        # Mudamos a fk de user na request por id
        # Ex: Usuario.user = User.id
        request.data['user'] = u.id

        # Chamamos a função de hashing sobre a senha
        hashed_password = password.hash_this(request.data['senha'])

        # Finalmente pode-se criar o serializer correspondente ao usuario
        serializer = UsuarioSerializer(data = request.data)

        # Se o serializer é valido receberá a senha com o hashing feito
        if serializer.is_valid(): 
            serializer.validated_data['senha'] = hashed_password 

        # Se o serializer permanecer válido podemos salvos o novo user e o novo usuário
        if serializer.is_valid():
            u.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #Sucedeu

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Falhou

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UsuarioDetail(APIView):
    """

    Acessa um usuário específico com sua id, pode editar e deletar.

    """
    # Função que retorna um objeto Usuário
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk = pk)
        except Usuario.DoesNotExist:
            raise Http404

    # Função que retorna os detalhes sobre um usuário específico
    def get(self, request, pk, format = None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    # Função que edita os valores de um usuário específico
    def put(self, request, pk, format = None):
        # Cria uma referência ao usuário escolhido
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data = request.data)
        
        # Se o serailizer for valido poderá editar os campos
        if serializer.is_valid():
            if request.data['login'] != usuario.login or request.data['email'] != usuario.email or request.data['senha'] != usuario.senha:
                user = User.objects.get(pk = usuario.user.pk)
                user.username = request.data['login']
                user.email = request.data['email']
                user.set_password(request.data['senha'])
                user.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Deleta um usuário e seu user associado
    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        u = User.objects.get(id = serializer.data['user'])
        u.delete()
        usuario.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)

############################ OCORRÊNCIA ##############################################
# CRUD ocorrências
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
# CRUD categoria
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
