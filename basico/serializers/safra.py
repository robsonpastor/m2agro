# -*- coding: utf-8 -*-
from basico.models.safra import Safra
from my_api.utils.serializer import MyApiSerializer


class SafraSerializer(MyApiSerializer):
    class Meta:
        model = Safra
        fields = ('id','nome', 'data_inicio', 'data_fim')
