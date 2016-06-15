# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 20:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('login', models.CharField(max_length=50, unique=True, verbose_name='Nome de Usuário')),
                ('cpf', models.BigIntegerField(blank=True, db_column='CPF', null=True, unique=True)),
                ('rg', models.IntegerField(blank=True, db_column='RG', null=True)),
                ('matricula', models.IntegerField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=1, null=True)),
                ('email', models.CharField(max_length=45)),
                ('senha', models.CharField(max_length=45)),
                ('status', models.IntegerField()),
                ('data_nasc', models.DateField(blank=True, null=True)),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
        ),
    ]
