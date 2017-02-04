# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from m2agro.utils.models import MyApiModel
from m2agro.utils.widgets import UpperCharField


class Safra(MyApiModel):
    nome        = UpperCharField('Nome', max_length=100)
    data_inicio = models.DateField(u'Data Início', null=True)
    data_fim    = models.DateField(u'Data Fim', null=True)
  
    def __unicode__(self):
        return self.nome
    class Meta:
        ordering = ['nome']
        verbose_name = "Produto"
        verbose_name_plural = 'Produtos'
        
