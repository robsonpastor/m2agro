# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers

from api_basico.views.produto_vw import  ProdutoSet
from api_basico.views.safra_vw import SafraSet


routes = routers.DefaultRouter(trailing_slash=False)
routes.register(r'produtos', ProdutoSet)
routes.register(r'safras', SafraSet)

urlpatterns = [
    url('', include(routes.urls)),
]
