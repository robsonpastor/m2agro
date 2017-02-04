# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.views import  ObtainJSONWebToken

from api_basico.models.usuario import Usuario
from api_basico.serializers.usuario import UsuarioSerializer


def my_api_jwt_response_payload_handler(token, user=None, request=None):
    usuario = Usuario.objects.get(pk=user.id)
    return {
        'access_token': token,
        'user': UsuarioSerializer(usuario).data
    }

class MyApiObtainJSONWebToken(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = my_api_jwt_response_payload_handler(token, user, request)
            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)