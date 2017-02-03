# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers

from api_servico.views.servico_vw import ServicoSet


routes = routers.DefaultRouter(trailing_slash=False)
routes.register(r'servicos', ServicoSet)

urlpatterns = [
    url('', include(routes.urls)),
]
