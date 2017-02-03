# -*- coding: utf-8 -*-

from basico.models.produto import Produto
from basico.serializers.produto import ProdutoSerializer
from my_api.utils.views import MyApiViewSet


class ProdutoSet(MyApiViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    