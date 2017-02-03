# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from api_basico.models.produto import Produto
from api_servico.models.servico import Servico
from m2agro.utils.models import MyApiModel


class ServicoItem(MyApiModel):
    produto        = models.ForeignKey(Produto,related_name='servico_itens')
    servico        = models.ForeignKey(Servico, related_name='servico_itens')
    quantidade     = models.DecimalField(u'Quantidade', max_digits=10, decimal_places=2)
    custo_item     = models.DecimalField(u'Custo', max_digits=10, decimal_places=2)
  
    def __unicode__(self):
        return self.produto.nome
    class Meta:
        ordering = ['produto__nome']
        verbose_name = u'Item de Serviço'
        verbose_name_plural = u'Itens de Serviços'
        
