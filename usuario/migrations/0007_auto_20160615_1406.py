# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 17:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='data_nasc',
            field=models.DateField(blank=True, null=True, verbose_name='data de nascimento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='grupo_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='tipo de usuário'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario e Senha'),
        ),
    ]
