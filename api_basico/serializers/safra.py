# -*- coding: utf-8 -*-
from api_basico.models.safra import Safra
from m2agro.utils.serializer import MyApiSerializer


class SafraSerializer(MyApiSerializer):
    class Meta:
        model = Safra
        fields = ('id','nome', 'data_inicio', 'data_fim')
