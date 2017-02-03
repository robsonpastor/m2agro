# -*- coding: utf-8 -*-
from basico.models.usuario import Usuario
from my_api.utils.serializer import MyApiSerializer


class UsuarioSerializer(MyApiSerializer):
    class Meta:
        model = Usuario
        fields = ('id','username',  'email','nome','cpf','orgao_expedidor','rg','password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = Usuario(
            email=validated_data['email'],
            username=validated_data['username'],
            nome=validated_data['nome'],
            cpf=validated_data['cpf'],
        #    orgao_expedidor=validated_data['orgao_expedidor'],
         #   rg=validated_data['rg']
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        valid_fields = self.writable_fields()
        for attr  in valid_fields:
            if (attr=='password' ):
                if validated_data.get('password',False):
                    instance.set_password(validated_data['password'])
            else:
                setattr(instance, attr, validated_data[attr])
                
        instance.save()
        return instance