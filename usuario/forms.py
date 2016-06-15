from django import forms
from django.contrib.auth.models import User, Group
from django.db import transaction
from django.forms import ModelForm, ValidationError
from django.contrib.auth.forms import AuthenticationForm
import datetime

from .models import Usuario


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username", max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'name': 'username'}))

    password = forms.CharField(
        label="Password", max_length=30,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'name': 'password'}))


class UsuarioForm(ModelForm):
    senha = forms.CharField(
        max_length=45,
        label='Senha',
        widget=forms.PasswordInput())

    confirma_senha = forms.CharField(
        max_length=45,
        label='Confirmar Senha',
        widget=forms.PasswordInput())

    confirma_email = forms.CharField(
        max_length=45,
        label='Confirmar Email')

    data_nasc = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Usuario
        fields = ['login',
                  'email',
                  'nome',
                  'senha',
                  'confirma_senha',
                  'confirma_email',
                  'cpf',
                  'rg',
                  'matricula',
                  'sexo',
                  'status',
                  'data_nasc',
                  'grupo_usuario']

        widgets = {'status': forms.HiddenInput(),
                   'grupo_usuario': forms.HiddenInput()}

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    def clean(self):

        if ('senha' not in self.cleaned_data or
                'confirma_senha' not in self.cleaned_data):
            raise ValidationError('Favor informar senhas atuais ou novas')

        msg = 'As senhas não conferem.'
        self.valida_igualdade(
            self.cleaned_data['senha'],
            self.cleaned_data['confirma_senha'],
            msg)

        if ('email' not in self.cleaned_data or
                'confirma_email' not in self.cleaned_data):
            raise ValidationError('Favor informar endereços de email')

        msg = 'Os emails não conferem.'
        self.valida_igualdade(
            self.cleaned_data['email'],
            self.cleaned_data['confirma_email'],
            msg)

        if self.cleaned_data['cpf'] != '' and len(self.cleaned_data['cpf']) != 14:
            raise ValidationError('CPF deve ter 11 dígitos')

        if len(self.cleaned_data['matricula']) > 10:
            raise ValidationError(
                'A matrícula deve ter ter no máximo 9 números')

        msg = 'As senhas não conferem.'
        self.valida_igualdade(
            self.cleaned_data['senha'],
            self.cleaned_data['confirma_senha'],
            msg)

        return self.cleaned_data

    @transaction.atomic
    def save(self, commit=False):
        usuario = super(UsuarioForm, self).save(commit)

        u = User.objects.create(
            username=usuario.login,
            email=usuario.email)
        u.set_password(self.cleaned_data['senha'])
        u.save()

        usuario.user = u
        usuario.save()

        grupo = Group.objects.get(name='Usuário Comum')
        u.groups.add(grupo)

        return usuario
