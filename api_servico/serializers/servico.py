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

    def save_servico_itens(self, servico, servico_itens_data):
        ids = []
        custo_total = 0
        for item_data in servico_itens_data:
            servico_item = self.fill_save_model(ServicoItem(servico=servico), item_data)
            custo_total += servico_item.custo_item
            ids.append(servico_item.id)
        
        if servico.custo_total != custo_total:
            servico.custo_total = custo_total
            servico.save()
        return ids

    def update(self, instance, validated_data):
        servico_itens_data = validated_data.pop('servico_itens', [])
        instance = super(ServicoSerializer, self).update(instance,validated_data)
        
        ids = self.save_servico_itens(instance, servico_itens_data)
        ServicoItem.objects.filter(servico=instance).exclude(id__in=ids).delete()
        return instance
        
    def create(self, validated_data):
        servico_itens_data = validated_data.pop('servico_itens', [])
        instance = super(ServicoSerializer, self).create(validated_data)
        
        self.save_servico_itens(instance, servico_itens_data)
        
        return instance