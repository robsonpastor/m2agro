# -*- coding: utf-8 -*- 
from django.db import models
from django.core.validators import RegexValidator

class UpperCharField( models.CharField):
    def get_prep_value(self, value):
        value = super(UpperCharField, self).get_prep_value(value)
        if value:
            return value.upper()
        else:
            value
class NumberCharField( models.CharField):
    regex_numeric = RegexValidator(r'^[0-9]*$', 'Somente números são permitidos neste campo.')
    default_validators = [regex_numeric]
