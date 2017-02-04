# -*- coding: utf-8 -*-

import datetime

from django.db.models.aggregates import Sum
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import list_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer

from api_basico.models.produto import Produto
from api_basico.serializers.produto import ProdutoSerializer
from api_servico.models.servico_item import ServicoItem
from m2agro.utils.date import lenient_date, add_months
from m2agro.utils.views import MyApiViewSet


class ProdutoSet(MyApiViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    
    
    @list_route(methods=['get'],authentication_classes=[BasicAuthentication],  url_path='integracao'
                ,renderer_classes=[XMLRenderer,JSONRenderer])
    def integracao(self, request, *args, **kwargs):
        return self.list( request, *args, **kwargs)
    
    @list_route(methods=['get'],authentication_classes=[BasicAuthentication],  url_path='calcula-preco-medio')
    def calcula_preco_medio(self, request, *args, **kwargs):
        fim = datetime.datetime.today()
        fim = lenient_date(fim.year, fim.month, 1)
        inicio = add_months(fim, -1)
        servicos_itens = ServicoItem.objects.filter(servico__data_inicio__gte=inicio
                               ,servico__data_inicio__lt=fim).values('produto').annotate(preco_medio=Sum('custo_item')/Sum('quantidade'))
        i = 0            
        for servico_item in servicos_itens:
            produto = Produto.objects.get(pk=servico_item['produto'])
            produto.preco_medio = servico_item['preco_medio']
            produto.save()
            i = i+1
            
                         
        return Response({'mensagem':[u'Cálculo referente ao mês de {}/{} realizado com sucesso. Total de  {} produtos atualizados'.format(inicio.month,inicio.year,i)]}, status=status.HTTP_200_OK)
        
    