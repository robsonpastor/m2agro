# -*- coding: utf-8 -*-
from django.db import models
class MyApiModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def save(self, *args, **kw):
        if self.pk is not None and self.created_at is None:
            original = self.__class__.objects.get(pk=self.pk)
            self.created_at = original.created_at
        super(MyApiModel, self).save( *args, **kw)