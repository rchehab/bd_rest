
***********************************************
# UNB-ALERTA API - BD REST
***********************************************
Projeto de um site que visa aumentar a segurança da UnB. Feito por alunos do 1/2016 de Linguagens de Programação. 

API DO SITE UNB ALERTA

* Crie um virtualenv wrapper usando python 3 e ative-o seguindo os passos abaixo:
    
    virtualenv -p /usr/bin/python3 --system-site-packages venv
    
    source venv/bin/activate
    
* Certifique-se que a partir deste passo, é apresentado no início da linha do prompt a expressão (venv).

    pip install djangorestframework
    
    pip install djangorestframework-jwt
    
    pip install django


* Com o dump do Banco do MySQL na pasta DB, execute:

    ./manage.py migrate

* Confira o funcionamento através do comando:

    ./manage.py runserver

* Em um navegador, acesse http://127.0.0.1:8000 e verifique o carregamento da página do projeto.

@ Funcionalidades:
- CRUD (criar, listar, editar, deletar) ocorrência
- CRUD (criar, listar, editar, deletar) usuários
- CRUD (criar, listar, editar, deletar) categorias
- CRUD (listar) grupos
- CRUD (listar) users
