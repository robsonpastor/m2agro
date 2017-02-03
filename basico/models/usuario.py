# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import models

from my_api.utils.widgets import UpperCharField,NumberCharField


class Usuario(models.User):
    nome            = UpperCharField(u'Nome', max_length=200, blank=True, null=True)
    cpf             = NumberCharField(u'CPF', max_length=11, blank=True, null=True)
    rg              = NumberCharField(u'RG', max_length=10, blank=True, null=True)
    orgao_expedidor = UpperCharField(u'Órgão Expedidor', max_length=50, blank=True, null=True)
    endereco         = UpperCharField(u'Endereço', max_length=200, blank=True, null=True)
    def __unicode__(self):
        return self.username
    class Meta:
        ordering = ['nome']
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'
        
