# -*- coding: utf-8 -*- 
# URLS DA API - UNB ALERTA - REST FRAMEWORK

from django.conf.urls import url

# Importando as views que serão utilizadas
from .views import (
    UserDetailAPIView,
    UserListAPIView,
    GroupDetailAPIView,
    GroupListAPIView,
    UsuarioList,
    UsuarioDetail,
    UsuarioDelete,
    UsuarioEdit,
    UsuarioCreate,
    OcorrenciaCreateAPIView,
    OcorrenciaDetailAPIView,
    OcorrenciaListAPIView,
    OcorrenciaUpdateAPIView,
    OcorrenciaDeleteAPIView,
    CategoriaCreateAPIView,
    CategoriaDetailAPIView,
    CategoriaListAPIView,
    CategoriaUpdateAPIView,
    CategoriaDeleteAPIView,
    LocalCreateAPIView,
    LocalDetailAPIView,
    LocalListAPIView,
    LocalUpdateAPIView,
    LocalDeleteAPIView
)

# Urls que seguem da extensão api
urlpatterns = [
    
    ############################ USER ##############################################
    # Acesso a lista de usuários nativos do Django e seus detalhes
    url(r'^user$', UserListAPIView.as_view(), name="User List"),
    url(r'^user/(?P<pk>\d+)/$', UserDetailAPIView.as_view(), name="User Detail"),

    ############################ GROUP ##############################################
    # Acesso a lista de grupos de users nativos do Django e seus detalhes
    url(r'^group$', GroupListAPIView.as_view(), name="Group List"),
    url(r'^group/(?P<pk>\d+)/$', GroupDetailAPIView.as_view(), name="Group Detail"),

    ############################ USUÁRIO ##############################################
    # Acesso  a lista de usuários e seus detalhes
    url(r'^usuario$', UsuarioList.as_view() , name = "Usuario List"),
    url(r'^usuario/create/$', UsuarioCreate.as_view(), name = "Create Usuario" ),
    url(r'^usuario/(?P<pk>\d+)/$', UsuarioDetail.as_view(), name = "UsuarioDetail"),
    url(r'^usuario/(?P<pk>\d+)/edit/$', UsuarioEdit.as_view(), name = "Usuario Update"),
    url(r'^usuario/(?P<pk>\d+)/delete/$', UsuarioDelete.as_view(), name = "Usuario Delete"),

    ############################ OCORRÊNCIA ##############################################
    # Acesso a lista de ocorrências e seus detalhes
    # Bem como as funções create, retrieve, edit e delete
    url(r'^ocorrencia$', OcorrenciaListAPIView.as_view(), name="Ocorrencia List"),
    url(r'^ocorrencia/create/$', OcorrenciaCreateAPIView.as_view(), name= "Create Ocorrencia"),
    url(r'^ocorrencia/(?P<pk>\d+)/$', OcorrenciaDetailAPIView.as_view(), name="Ocorrencia Detail"),
    url(r'^ocorrencia/(?P<pk>\d+)/edit/$', OcorrenciaUpdateAPIView.as_view(), name="Ocorrencia Update"),
    url(r'^ocorrencia/(?P<pk>\d+)/delete/$', OcorrenciaDeleteAPIView.as_view(), name="Ocorrencia Delete"),


    ########################### CATEGORIA ##############################################
    # Acesso a lista de categorias das ocorrências e seus detalhes
    # Bem como as funções create, retrieve, edit e delete
    url(r'^categoria$', CategoriaListAPIView.as_view(), name="Categoria List"),
    url(r'^categoria/create/$', CategoriaCreateAPIView.as_view(), name= "Create Categoria"),
    url(r'^categoria/(?P<pk>\d+)/$', CategoriaDetailAPIView.as_view(), name="Categoria Detail"),
    url(r'^categoria/(?P<pk>\d+)/edit/$', CategoriaUpdateAPIView.as_view(), name="Categoria Update"),
    url(r'^categoria/(?P<pk>\d+)/delete/$', CategoriaDeleteAPIView.as_view(), name="Categoria Delete"),
    

    ########################### Locais ##############################################
    # Acesso a lista de Locals das ocorrências e seus detalhes
    # Bem como as funções create, retrieve, edit e delete
    url(r'^local$', LocalListAPIView.as_view(), name="Local List"),
    url(r'^local/create/$', LocalCreateAPIView.as_view(), name= "Create Local"),
    url(r'^local/(?P<pk>\d+)/$', LocalDetailAPIView.as_view(), name="Local Detail"),
    url(r'^local/(?P<pk>\d+)/edit/$', LocalUpdateAPIView.as_view(), name="Local Update"),
    url(r'^local/(?P<pk>\d+)/delete/$', LocalDeleteAPIView.as_view(), name="Local Delete"),
    
]
