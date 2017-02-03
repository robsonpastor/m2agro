# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from my_api.utils.models import MyApiModel
from my_api.utils.widgets import UpperCharField


class Produto(MyApiModel):
    nome     = UpperCharField('Nome', max_length=100, unique=True)
    preco_medio    = models.DecimalField(u'Preço Médio', max_digits=10, decimal_places=2, null=True)
  
    def __unicode__(self):
        return self.nome
    class Meta:
        ordering = ['nome']
        verbose_name = "Produto"
        verbose_name_plural = 'Produtos'
        
