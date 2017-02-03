# -*- coding: utf-8 -*-
from basico.models.produto import  Produto
from my_api.utils.serializer import MyApiSerializer


class ProdutoSerializer(MyApiSerializer):
    class Meta:
        model = Produto
        fields = ('id','nome',  'preco_medio')
        extra_kwargs = {'preco_medio': {'read_only': True}}