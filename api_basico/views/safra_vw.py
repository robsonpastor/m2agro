# -*- coding: utf-8 -*-

from api_basico.models.safra import Safra
from api_basico.serializers.safra import SafraSerializer
from m2agro.utils.views import MyApiViewSet


class SafraSet(MyApiViewSet):
    queryset = Safra.objects.all()
    serializer_class = SafraSerializer

    