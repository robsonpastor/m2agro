# -*- coding: utf-8 -*-

from basico.models.safra import Safra
from basico.serializers.safra import SafraSerializer
from m2agro.utils.views import MyApiViewSet


class SafraSet(MyApiViewSet):
    queryset = Safra.objects.all()
    serializer_class = SafraSerializer

    