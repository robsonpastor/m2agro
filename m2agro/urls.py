"""m2agro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from m2agro.utils.auth_jwt import MyApiObtainJSONWebToken


urlpatterns = [
    url(r'^admin', admin.site.urls),
 
    
    url(r'^v1.0/auth', MyApiObtainJSONWebToken.as_view()),
    url(r'^v1.0/basico/', include('api_basico.urls')),
    url(r'^v1.0/servico/', include('api_servico.urls')),
]
