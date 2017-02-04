# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-03 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_servico', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servico',
            options={'ordering': ['nome'], 'verbose_name': 'Servi\xe7o', 'verbose_name_plural': 'Servi\xe7os'},
        ),
        migrations.AddField(
            model_name='servico',
            name='custo_total',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Custo Total'),
        ),
    ]