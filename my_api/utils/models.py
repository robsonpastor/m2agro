# -*- coding: utf-8 -*-
from django.utils.timezone import utc
import datetime
from django.db import models


class MyApiModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,default=datetime.datetime(2016, 9, 9, 11, 15, 15, 666614, tzinfo=utc))
    updated_at = models.DateTimeField(auto_now=True,default=datetime.datetime(2016, 9, 9, 11, 15, 15, 666614, tzinfo=utc))

    class Meta:
        abstract = True

