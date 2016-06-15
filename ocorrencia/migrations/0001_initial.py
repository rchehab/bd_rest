# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-24 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'tb_categoria',
            },
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'tb_localizacao',
            },
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora', models.DateTimeField()),
                ('descricao', models.TextField(blank=True, null=True)),
                ('foto', models.CharField(blank=True, max_length=45, null=True)),
                ('validade', models.CharField(max_length=1)),
                ('atendida', models.IntegerField()),
                ('emergencia', models.IntegerField()),
                ('vitimado', models.IntegerField()),
                ('resposta', models.CharField(blank=True, max_length=45, null=True)),
                ('usuario_id', models.IntegerField(db_column='usuario_ID')),
                ('vigilante_id', models.IntegerField(db_column='vigilante_ID')),
                ('tb_categoria_id', models.IntegerField(db_column='tb_categoria_ID')),
                ('tb_localizacao_id', models.IntegerField(db_column='tb_localizacao_ID')),
            ],
            options={
                'verbose_name_plural': 'Ocorrências',
                'managed': False,
                'verbose_name': 'Ocorrência',
                'db_table': 'tb_ocorrencia',
            },
        ),
    ]
