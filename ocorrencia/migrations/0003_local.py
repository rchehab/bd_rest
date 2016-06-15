# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0002_auto_20160526_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=45)),
                ('pai', models.IntegerField(blank=True, db_column='pai', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'tb_local',
            },
        ),
    ]
