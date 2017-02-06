# -*- coding: utf-8 -*-

from m2agro.utils.views import MyApiViewSet
from api_servico.models.servico import Servico
from api_servico.serializers.servico import ServicoSerializer


class ServicoSet(MyApiViewSet):
    queryset = Servico.objects.all().prefetch_related('safra')
    serializer_class = ServicoSerializer

    