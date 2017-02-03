# -*- coding: utf-8 -*-
from rest_framework import serializers  



class MyApiSerializer(serializers.ModelSerializer):
    def model_serialized_fields(self):
        serializer_fields = self.Meta.fields
        model_fields = {f.name: f for f in self.Meta.model._meta.get_fields()}
        fields = [] 
        for field_name in  serializer_fields:
            if  field_name in model_fields:
                fields.append(model_fields[field_name])
        return fields
    
    def read_only_field(self, field_name):
        try:
            serializer_fields = self.Meta.extra_kwargs
            return serializer_fields[field_name]['read_only']
        except:
            return False
        
    def writable_fields(self):
        fields = []
        for field in self.model_serialized_fields():
            if field.concrete and not field.auto_created and not self.read_only_field(field.name):
                fields.append(field.name) 
        return fields
        
    def fill_save_model(self, model, data):
        for attr in data:
            setattr(model, attr, data[attr])
        model.save()
        return model
    def unique_validator(self, items, field):
        items_dict = {}
        errors = []
        has_errors = False
        for item  in items:
            error = {}
            if(items_dict.get(item[field],False)):
                error = {field:[u'Este campo não pode ser cadastrado em duplicidade']}
                has_errors = True
            errors.append(error)
            items_dict[item[field]]= True
        if has_errors:
            raise serializers.ValidationError(errors)
        return items