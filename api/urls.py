# -*- coding: utf-8 -*- 
from django.conf.urls import url

from .views import(
    UserCreateAPIView,
    UserDetailAPIView,
    UserListAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    UsuarioCreateAPIView,
    UsuarioDetailAPIView,
    UsuarioListAPIView,
    UsuarioUpdateAPIView,
    UsuarioDeleteAPIView,
    OcorrenciaCreateAPIView,
    OcorrenciaDetailAPIView,
    OcorrenciaListAPIView,
    OcorrenciaUpdateAPIView,
    OcorrenciaDeleteAPIView,
    )

urlpatterns = [

    url(r'^user$', UserListAPIView.as_view(), name="User List"),
    url(r'^user/create/$', UserCreateAPIView.as_view(), name= "Create User"),
    url(r'^user/(?P<pk>\d+)/$', UserDetailAPIView.as_view(), name="User Detail"),
    url(r'^user/(?P<pk>\d+)/edit/$', UserUpdateAPIView.as_view(), name="User Update"),
    url(r'^user/(?P<pk>\d+)/delete/$',UserDeleteAPIView.as_view(), name="User Delete"),

    url(r'^usuario$', UsuarioListAPIView.as_view(), name="Usuario List"),
    url(r'^usuario/create/$', UsuarioCreateAPIView.as_view(), name= "Create Usuario"),
    url(r'^usuario/(?P<pk>\d+)/$', UsuarioDetailAPIView.as_view(), name="Usuario Detail"),
    url(r'^usuario/(?P<pk>\d+)/edit/$', UsuarioUpdateAPIView.as_view(), name="Usuario Update"),
    url(r'^usuario/(?P<pk>\d+)/delete/$',UsuarioDeleteAPIView.as_view(), name="Usuario Delete"),

    url(r'^ocorrencia$', OcorrenciaListAPIView.as_view(), name="Ocorrencia List"),
    url(r'^ocorrencia/create/$', OcorrenciaCreateAPIView.as_view(), name= "Create Ocorrencia"),
    url(r'^ocorrencia/(?P<pk>\d+)/$', OcorrenciaDetailAPIView.as_view(), name="Ocorrencia Detail"),
    url(r'^ocorrencia/(?P<pk>\d+)/edit/$', OcorrenciaUpdateAPIView.as_view(), name="Ocorrencia Update"),
    url(r'^ocorrencia/(?P<pk>\d+)/delete/$', OcorrenciaDeleteAPIView.as_view(), name="Ocorrencia Delete"),

]
