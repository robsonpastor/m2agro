# -*- coding: utf-8 -*-

from basico.models.produto import Produto
from basico.serializers.produto import ProdutoSerializer
from m2agro.utils.views import MyApiViewSet


class ProdutoSet(MyApiViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    