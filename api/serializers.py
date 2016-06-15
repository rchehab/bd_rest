# -*- coding: utf-8 -*- 
# SERIALIZERS DA API - UNB ALERTA - REST FRAMEWORK


# Importando os models preestabelecidos pelo Django e os models do UnB Alerta
from usuario.models import Usuario
from ocorrencia.models import Categoria, Ocorrencia, Local
from django.contrib.auth.models import User, Group

from rest_framework import serializers

############################ USER ##############################################
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')

############################ GROUP ##############################################
class GroupSerializer(serializers.ModelSerializer):

    class Meta:
      model = Group
      fields = ('id', 'name')

############################ USUÁRIO ##############################################
class UsuarioSerializer(serializers.ModelSerializer):

  nome = serializers.CharField(
    max_length=45, 
    allow_blank=False, 
    label='Nome Completo',
  )

  login = serializers.CharField(
    max_length=45,
    allow_blank=False,
    label='Login',
  )

  senha = serializers.CharField(
    style={'input_type': 'password'}
  )

  cpf = serializers.CharField(
    max_length=45,
    allow_blank=False,
    label='CPF',
  )

  rg = serializers.CharField(
    label='RG',
  )

  matricula = serializers.IntegerField(
    label='Matrícula',
  ) 

  email = serializers.EmailField(
    max_length=45, 
    allow_blank=False,
    label='Email',
  )

  sexo = serializers.ChoiceField(
    choices=['M','F', 'm', 'f'],
  
  )

  data_nasc = serializers.DateField(
    format='iso-8601', 
    input_formats=None, 
    label='Data de Nascimento',
  )

  class Meta:
    model = Usuario
    fields = ( 'id', 'cpf', 'nome', 'rg','matricula','sexo','email','login','senha','status',
                  'data_nasc','user', 'grupo_usuario',)

############################ OCORRÊNCIA ##############################################
class OcorrenciaSerializer(serializers.ModelSerializer):

  data = serializers.DateField(
    format = 'iso-8601', 
    input_formats = None, 
    label = 'Data da Ocorrência',
  )

  hora = serializers.TimeField(
    format = 'iso-8601', 
    input_formats = None, 
    label = 'Hora da Ocorrência',
  )

  descricao = serializers.CharField(
    allow_blank = True, 
    max_length = None,
    min_length = None,
    label = 'Descrição',
  )

  resposta = serializers.CharField(
    allow_blank=True, 
    min_length=None, 
    max_length=20,
    label = 'Resposta',
  )

  validade = serializers.NullBooleanField(
    label = 'Validade',
  )

  emergencia = serializers.NullBooleanField(
    label = 'Emergência',

  )

  class Meta:
    model = Ocorrencia
    fields = ( 'id', 'data', 'hora', 'latitude', 'longitude', 'descricao', 'foto', 'validade',
                'atendida', 'emergencia', 'vitimado', 'repetida', 'resposta', 'usuario_ID', 'tb_categoria_ID', 'tb_local_ID')
            
############################ CATEGORIA ##############################################
class CategoriaSerializer(serializers.ModelSerializer):

  class Meta:
      model = Categoria
      fields = ('id', 'descricao')

############################ LOCAL ##############################################
class LocalSerializer(serializers.ModelSerializer):

  class Meta:
    model = Local
    fields = ('id', 'nome', 'pai', 'descricao')
