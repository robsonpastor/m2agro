# API RESTFul M2Agro 

Este projeto é referente a uma API RESTFul desenvolvida em caráter de teste para a M2Agro.
O Projeto contempla os seguintes requisitos:
- API RESTFul Json
- API com CRUD de Produtos e de Safra
- API com CRUD de Serviços/Itens de Serviço com o custo total sendo calculado internamente em função dos itens. 
- Rotina de Cálculo dos Preços Médios de produtos em função do mês anterior
- API de integração dos Preços Médios de Produtos com sistemas externos e com a possibilidade de formatos diversos.


### Prerequisitos

Python 2.7 instalado
Pip install instalado
Banco de dados PostgreSQL 9.4 ou superior


### Instalação
Instale os requisitos python
```
$ pip install -r requirements.txt
```
Crie o arquivo m2agro/settings.py a partir do m2agro/settings.py.sample
```
$ cp m2agro/settings.py.sample m2agro/settings.py
```
Abra o arquivo m2agro/settings.py para configurar o Banco de Dados. Defina os valores das variáveis  NAME, USER, PASSWORD, HOST e PORT com o nome do banco, nome do usuário, senha do usuário, host do banco e porta de conexão, respectivamente
```
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2', 
        'NAME':'<name_db>',
        'USER':'<user_db>',
        'PASSWORD':'<password_db>',
        'HOST':'<host_db>',
        'PORT':'<port_db>',
        },
}
```

Crie a estrutura de Banco de Dados
```
$ python manage.py migrate
```

Crie um usuário para acessar a API.
```
$ python manage.py createsuperuser
```


Rode a aplicação.
```
$ python manage.py runserver
```

## Autenticação

Para a autenticação, um objeto json deve ser enviado via método PUT para a url
[http://localhost:8000/v1.0/auth](http://localhost:8000/v1.0/auth) 

O objeto deve atender a seguinte estrutura:

```
{
    "username": "<nome do usuario>",
    "password": "<senha do usuario>"
}
```
O Header das requisições conter a chave Autorization com o valor 'Bear <token_retornado>'


Por tratar-se de um ambiente de testes, o usuário também pode acessar diretamente pelo navegador através do link
[http://localhost:8000/admin](http://localhost:8000/admin)

## APIs
Após a autenticação é possível acessar as APIs 
As APIs dos recursos Produto, Safra e Serviço atendem a abordagem [RESTFul API](http://restfulapi.net/http-methods/)

API Básico
Produto
[http://localhost:8000/v1.0/basico/produtos](http://localhost:8000/v1.0/basico/produtos)
Safra
[http://localhost:8000/v1.0/basico/safras](http://localhost:8000/v1.0/basico/safras)

API Serviço
[http://localhost:8000/v1.0/servico/servicos](http://localhost:8000/v1.0/servico/servicos)

Para o Cálculo de preço médio referente aos lançamentos mês anterior uma requisição PUT deve ser enviada para a URL abaixo. 
http://localhost:8000/v1.0/basico/produtos/calcula-preco-medio

A integração de Preço Médio dos produtos é acessada através de uma requisição GET para a URL abaixo. Onde o parâmetro format 
pode ter os valores 'json' ou 'xml' de acordo com a necessidade.
http://localhost:8000/v1.0/basico/produtos/integracao?format=json



