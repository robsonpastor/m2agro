# -*- coding: utf-8 -*-

from functools import reduce
import operator

from django.db.models import Q
from django.db.models.deletion import ProtectedError
from rest_framework import viewsets, status
from rest_framework.response import Response


class MyApiViewSet(viewsets.ModelViewSet):
    def get_list_serializer_class(self):
        if not hasattr(self, 'list_serializer_class'):
            return self.serializer_class
        return self.list_serializer_class

    def get_list_serializer(self, *args, **kwargs):
        list_serializer_class = self.get_list_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return list_serializer_class(*args, **kwargs)
    

    def queryset_builder(self, request):
        sort_fields = request.GET.get('sort', None)
        boolean_operator = request.GET.get('operator', 'and')
        field_filter = {}
        for k, v in request.GET.items():
            if '__' in k:
                field_filter[k] = v
        
        queryset = self.filter_queryset(self.get_queryset())
        if boolean_operator == 'or':
            queryset = queryset.filter(reduce(operator.or_, 
                    (Q(**d) for d in [dict([i]) for i in field_filter.items()])))
        else:
            queryset = queryset.filter(**field_filter)
        if sort_fields:
            queryset = queryset.order_by(*sort_fields.split('|'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.queryset_builder(request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_list_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except ProtectedError:
            return Response(data={'non_field_errors': u'Não é possível excluir o registro. Registros filhos encontrados'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
    