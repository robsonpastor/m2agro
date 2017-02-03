# -*- coding: utf-8 -*-

from m2agro.utils.views import MyApiViewSet
from api_servico.models.servico import Servico
from api_servico.serializers.servico import ServicoSerializer
from api_basico.serializers.safra import SafraSerializer


class ServicoSet(MyApiViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    