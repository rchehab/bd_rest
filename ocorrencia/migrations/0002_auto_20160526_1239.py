# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='localizacao',
            options={'managed': False, 'verbose_name': 'Localização', 'verbose_name_plural': 'Localizações'},
        ),
    ]
