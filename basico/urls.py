# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers

from basico.views.produto_vw import  ProdutoSet


routes = routers.DefaultRouter(trailing_slash=False)
routes.register(r'produtos', ProdutoSet)

urlpatterns = [
    url('', include(routes.urls)),
]
