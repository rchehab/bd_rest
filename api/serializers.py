# -*- coding: utf-8 -*- 
from usuario.models import Usuario
from ocorrencia.models import Categoria, Ocorrencia
from rest_framework import serializers
from django.contrib.auth.models import User, Group

class CategoriaSerializer(serializers.ModelSerializer):

  class Meta:
      model = Categoria
      fields = ('id', 'tipo')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
      model = Group
      fields = ('id', 'name')

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

  rg = serializers.IntegerField(
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
    choices=['Masculino', 'Feminino'],
    
  )

  data_nasc = serializers.DateField(
    format='iso-8601', 
    input_formats=None, 
    label='Data de Nascimento',
  )

  class Meta:
    model = Usuario
    fields = [    'id',
		              'cpf',
                  'nome',
		              'rg',
                  'matricula',
                  'sexo',
                  'email',
                  'login',
                  'senha',
                  'status',
                  'data_nasc',
                  'user',
                  'grupo_usuario',
                  ]

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
    min_length = 20,
    label = 'Descrição',
  )

  resposta = serializers.CharField(
    allow_blank=True, 
    min_length=None, 
    max_length=20,
    label = 'Resposta',
  )

  emergencia = serializers.NullBooleanField(
    label = 'Emergência',

  )

  class Meta:
    model = Ocorrencia
    fields = [  'id',
                'data',
                'hora',
                'latitude',
                'longitude',
                'descricao', 
                'foto',
                'validade',
                'atendida',
                'emergencia',
                'vitimado',
                'repetida',
                'resposta',
                'usuario_ID',
                'vigilante_ID',
                'tb_categoriaID',
                
              ]
              
            
                