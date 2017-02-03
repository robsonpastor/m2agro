# -*- coding: utf-8 -*-
from api_servico.models.servico import Servico
from api_servico.models.servico_item import ServicoItem
from api_servico.serializers.servico_item import ServicoItemSerializer
from m2agro.utils.serializer import MyApiSerializer


class ServicoSerializer(MyApiSerializer):
    servico_itens = ServicoItemSerializer(many=True)
    class Meta:
        model = Servico
        fields = ('id','nome', 'data_inicio', 'data_fim', 'safra', 'servico_itens', 'custo_total')
        extra_kwargs = {'custo_total':{'read_only':True}}
    def update(self, instance, validated_data):
        valid_fields = self.writable_fields()
        ids = []
        for attr  in valid_fields:
            setattr(instance, attr, validated_data[attr])
        instance.save()
        custo_total = 0
        for item_data in validated_data['servico_itens']:
            servico_item = self.fill_save_model(ServicoItem( servico=instance),item_data)
            custo_total+=servico_item.custo_item
            ids.append(servico_item.id)
        
        if instance.custo_total != custo_total:
            instance.custo_total = custo_total
            instance.save()
        ServicoItem.objects.filter(servico=instance).exclude(id__in=ids).delete()
        return instance
        
    def create(self, validated_data):
        servico_itens_data = validated_data.pop('servico_itens', [])
        instance = super(ServicoSerializer, self).create(validated_data)
        servico_itens = []
        custo_total = 0
        for item_data in servico_itens_data:
            servico_item = self.fill_save_model(ServicoItem( servico=instance),item_data)
            servico_itens.append( servico_item)
            custo_total+=servico_item.custo_item
        if instance.custo_total != custo_total:
            instance.custo_total = custo_total
            instance.save()
        instance.servico_itens = servico_itens
        return instance