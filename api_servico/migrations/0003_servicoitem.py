# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-03 18:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api_basico', '0002_safra'),
        ('api_servico', '0002_auto_20170203_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 9, 11, 15, 15, 666614, tzinfo=utc))),
                ('updated_at', models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 9, 9, 11, 15, 15, 666614, tzinfo=utc))),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Quantidade')),
                ('custo_item', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Custo')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servico_itens', to='api_basico.Produto')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servico_itens', to='api_servico.Servico')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Item de Servi\xe7o',
                'verbose_name_plural': 'Itens de Servi\xe7os',
            },
        ),
    ]