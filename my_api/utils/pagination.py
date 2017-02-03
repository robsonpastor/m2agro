# -*- coding: utf-8 -*-
from rest_framework import pagination
from rest_framework.response import Response
from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
from django.utils import six

class MyApiPagination(pagination.PageNumberPagination):
    page_size = 100
    max_page_size = 1000
    header_total_pages = 'x-total' 
    header_next_page = 'next' 
    header_previous_pages = 'previous' 
    page_size_query_param = 'page_size'
    header_page_size_param = 'HTTP_X_PER_PAGE'
    header_page_number_param = 'HTTP_PAGE'
    def get_paginated_response(self, data):
        headers = {}
        headers[self.header_total_pages] = self.page.paginator.count
        if self.page.has_previous():
            headers[self.header_previous_pages] = self.page.previous_page_number()
        if self.page.has_next():
            headers[self.header_next_page] = self.page.next_page_number()
        return Response(
             data,headers=headers
        )
    def get_page_size(self, request):
        if self.header_page_size_param in request.META.keys():
            return pagination._positive_int(
                    request.META[self.header_page_size_param],
                    strict=True,
                    cutoff=self.max_page_size
                )
        
        elif self.page_size_query_param:
            try:
                return pagination._positive_int(
                    request.query_params[self.page_size_query_param],
                    strict=True,
                    cutoff=self.max_page_size
                )
            except (KeyError, ValueError):
                pass

        return self.page_size
    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        if self.header_page_number_param in request.META.keys():
            page_number = request.META[self.header_page_number_param]
        else:
            page_number = request.query_params.get(self.page_query_param, 1)
            
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=six.text_type(exc)
            )
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)