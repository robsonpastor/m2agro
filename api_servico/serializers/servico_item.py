# -*- coding: utf-8 -*-
from rest_framework import serializers

from m2agro.utils.serializer import MyApiSerializer
from api_servico.models.servico_item import ServicoItem


class ServicoItemSerializer(MyApiSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = ServicoItem
        fields = ('id','produto', 'custo_item', 'quantidade')
