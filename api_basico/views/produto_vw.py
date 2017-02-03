# -*- coding: utf-8 -*-

from api_basico.models.produto import Produto
from api_basico.serializers.produto import ProdutoSerializer
from m2agro.utils.views import MyApiViewSet


class ProdutoSet(MyApiViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    