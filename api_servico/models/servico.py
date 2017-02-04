# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from api_basico.models.safra import Safra
from m2agro.utils.models import MyApiModel
from m2agro.utils.widgets import UpperCharField


class Servico(MyApiModel):
    nome        = UpperCharField('Nome', max_length=100)
    data_inicio = models.DateField(u'Data Início', null=True)
    data_fim    = models.DateField(u'Data Fim', null=True)
    safra       = models.ForeignKey(Safra)
    custo_total = models.DecimalField(u'Custo Total', max_digits=12, decimal_places=2, null=True)
  
    def __unicode__(self):
        return self.nome
    class Meta:
        ordering = ['nome']
        verbose_name = u'Serviço'
        verbose_name_plural = u'Serviços'
        
