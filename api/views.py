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
from ocorrencia.models import Categoria, Ocorrencia, Local

# Importando os serializers de cada classe usada
from api.serializers import (

    UsuarioSerializer, 
    OcorrenciaSerializer, 
    CategoriaSerializer, 
    UserSerializer, 
    GroupSerializer,
    LocalSerializer

    )

# Importando arquivo com as permissões de User 
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Importando classe password, utilizada para o hashing da senha
from api.password import password

# Outros imports 
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


############################ USER ##############################################
# Listagem de Users internos do Django bem quanto seus detalhes.
# Permissão: Só quem tem acesso é o Admin
class UserDetailAPIView(RetrieveAPIView):
    '''
    
    Detalhes dos users
    
    '''
    queryset = User.objects.all() # Retorna todos os User
    serializer_class = UserSerializer # Utiliza a classe serializer User
    #permission_classes = (permissions.IsAdminUser,) 

class UserListAPIView(ListAPIView):
    '''
    
    Lista dos users
    
    '''
    queryset = User.objects.all() # Retorna todos os User
    serializer_class = UserSerializer # Utiliza a classe serializer User
    #permission_classes = (permissions.IsAdminUser,)

############################ GROUP ##############################################
# CRUD Group
# Listagem de Groups internos do Django bem quanto seus detalhes.
# Permissão: Só quem tem acesso é o Admin
class GroupDetailAPIView(RetrieveAPIView):
    '''
    
    Detalhes dos grupos de users
    
    '''
    queryset = Group.objects.all() # Retorna todos os Groups
    serializer_class = GroupSerializer # Utiliza a classe serializer Group
   # permission_classes = (permissions.IsAdminUser,)


class GroupListAPIView(ListAPIView):
    '''
    
    Lista dos grupos de users
    
    '''
    queryset = Group.objects.all() # Retorna todos os Groups
    serializer_class = GroupSerializer # Utiliza a classe serializer Group
   #permission_classes = (permissions.IsAdminUser,)

############################ USUÁRIO ##############################################
# CRUD Usuário

# Lista de todos os usários
# Permissão: Quem tem acesso é o Admin
class UsuarioList(APIView):
    
    authentication_classes = (SessionAuthentication, BasicAuthentication)


    """

    Lista todos os usuários e permite a criação.

    """
    # Função get: Retorna todos os usuários do banco
    def get(self, request, format = None):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many = True)
        return Response(serializer.data)

    
# Criação de um novo usuário
# Permissão: liberado pra todos
class UsuarioCreate(APIView):
    """

    Lista todos os usuários e permite a criação.

    """
    # Função post: Cria um novo usuário 

    def post(self, request, format = None):
        
        u = User.objects.create(
                    username = request.data['login'], # Passamos o login
                    email = request.data['email'] # Passamos o email
                )

        u.set_password(request.data['senha'])

        request.data['user'] = u.id

        usuario = UsuarioSerializer(data = request.data)

        if usuario.is_valid():
            
            u.save()
            usuario.save()
            return Response(usuario.data, status=status.HTTP_201_CREATED) #Sucedeu

        return Response(usuario.errors, status=status.HTTP_400_BAD_REQUEST) #Falhou

    #permission_classes = (permissions.AllowAny,)

# Detalhes de um Usuário
# Permissão: liberado para o próprio usuário e Admin *
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

# Edição de um usuário
# Permissão: liberado para o próprio usuário e admin*
class UsuarioEdit(APIView):
    """

    Edita um usuário específico

    """

    # Função que retorna os detalhes sobre um usuário específico
    def get(self, request, pk, format = None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)


    # Função que retorna um objeto Usuário
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk = pk)
        except Usuario.DoesNotExist:
            raise Http404

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

# Deletar um usuário
# Permissão liberada para o admin
class UsuarioDelete(APIView):

    # Função que retorna os detalhes sobre um usuário específico
    def get(self, request, pk, format = None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
        
    # Função que retorna um objeto Usuário
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk = pk)
        except Usuario.DoesNotExist:
            raise Http404

    # Deleta um usuário e seu user associado
    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        u = User.objects.get(id = serializer.data['user'])
        u.delete()
        usuario.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)

    #permission_classes(permissions.IsAdminUser)

############################ OCORRÊNCIA ##############################################
# CRUD ocorrências
# Criar uma nova ocorrência
# Permissão: qualquer usuário cadastrado
class OcorrenciaCreateAPIView(CreateAPIView):
    '''

    Crie uma nova ocorrência

    '''
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
   #permission_classes = (permissions.IsAuthenticated,)       

# Detalhes de uma ocorrência
# Permissão: dono da ocorrência, admin, vigilante*
class OcorrenciaDetailAPIView(RetrieveAPIView):
    '''

    Informações das ocorrências

    '''
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
   # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# Lista de ocorrências
# Permissão: usuario dono da ocorrencia, ocorrências validadas*
class OcorrenciaListAPIView(ListAPIView):
    '''

    Liste as ocorrências

    '''
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
   # permission_classes = (permissions.IsOwner,)

# Editar ocorrências
# Permissão: usuário dono da ocorrência se ela nao tiver sido validada, vigilante,admin*
class OcorrenciaUpdateAPIView(RetrieveUpdateAPIView):
    '''

    Edite ocorrência

    '''
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
   # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# Deletar ocorrência
# Permissão: usuário dono da ocorrência se ela não tiver sido validada, vigilante, admin*
class OcorrenciaDeleteAPIView(DestroyAPIView):
    '''
    Delete uma ocorrência
    '''
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
   # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

############################ CATEGORIA ##############################################
# CRUD Categoria
# Só tem acesso se o usuário for Admin
# Criar Admin, mudar no BD is_staff de um User para TRUE
# Permissão: Só quem tem acesso é o Admin
class CategoriaCreateAPIView(CreateAPIView):
    '''

    Crie uma nova categoria

    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
   # permission_classes = (permissions.IsAdminUser,)      

class CategoriaDetailAPIView(RetrieveAPIView):
    '''

    Informações das categorias

    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
   # permission_classes = (permissions.IsAdminUser,)

class CategoriaListAPIView(ListAPIView):
    '''

    Liste as categorias

    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
   # permission_classes = (permissions.IsAdminUser,)

class CategoriaUpdateAPIView(RetrieveUpdateAPIView):
    '''

    Edite uma categoria

    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
  #  permission_classes = (permissions.IsAdminUser,)

class CategoriaDeleteAPIView(DestroyAPIView):
    '''

    Delete uma categoria

    '''
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
   # permission_classes = (permissions.IsAdminUser,)

############################ LOCAL ##############################################
# CRUD Local
# Só tem acesso se o usuário for Admin
# Criar Admin, mudar no BD is_staff de um User para TRUE
# Permissão: Só quem tem acesso é o Admin
class LocalCreateAPIView(CreateAPIView):
    '''

    Crie uma nova local

    '''
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
   # permission_classes = (permissions.IsAdminUser,)      

class LocalDetailAPIView(RetrieveAPIView):
    '''

    Informações das locals

    '''
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
   # permission_classes = (permissions.IsAdminUser,)

class LocalListAPIView(ListAPIView):
    '''

    Liste as locals

    '''
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
   # permission_classes = (permissions.IsAdminUser,)

class LocalUpdateAPIView(RetrieveUpdateAPIView):
    '''

    Edite uma local

    '''
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
  #  permission_classes = (permissions.IsAdminUser,)

class LocalDeleteAPIView(DestroyAPIView):
    '''

    Delete uma local

    '''
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
   # permission_classes = (permissions.IsAdminUser,)
