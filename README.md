Gerenciador de Tarefas

Sistema web de gerenciamento de tarefas desenvolvido com Python, Django e MySQL, utilizando um quadro Kanban para organizar e acompanhar as atividades.

Funcionalidades

Cadastro de usuários.

Cadastro de tarefas.

Associação de tarefas aos usuários responsáveis.

Definição de setor e prioridade.

Atualização de status e prioridade.

Visualização das tarefas em um quadro Kanban com três etapas:

A fazer

Fazendo

Pronto

Tecnologias utilizadas

Python 3.14

Django 6.1.3

MySQL 8.4

HTML5

Bootstrap 5

Git e GitHub

Estrutura do banco de dados

O sistema possui duas entidades principais:

Usuario

id (PK)

nome

email

Tarefa

id (PK)

usuario_id (FK)

descricao

setor

prioridade

data_cadastro

status

Relacionamento: um usuário pode possuir várias tarefas, enquanto cada tarefa pertence a um único usuário (1).

O diagrama entidade-relacionamento está disponível no arquivo diagrama_gerenciador_tarefas.png.

Como executar o projeto

1. Clonar o repositório

git clone https://github.com/gslarie/gerenciador_tarefas.git
cd gerenciador_tarefas

2. Criar e ativar o ambiente virtual

python -m venv venv

Windows PowerShell:

.\venv\Scripts\Activate.ps1

3. Instalar as dependências

pip install -r requirements.txt

4. Configurar o banco de dados

Crie um banco de dados MySQL chamado gerenciador_tarefas.

Crie um arquivo .env na raiz do projeto com as seguintes configurações:

DJANGO_SECRET_KEY=sua_chave_secreta
DB_NAME=gerenciador_tarefas
DB_USER=root
DB_PASSWORD=sua_senha_mysql
DB_HOST=127.0.0.1
DB_PORT=3306

Substitua os valores de exemplo pelas suas próprias configurações locais.

5. Executar as migrações

python manage.py migrate

6. Iniciar o servidor

python manage.py runserver

Acesse no navegador:

http://127.0.0.1:8000/

Banco de dados

O arquivo gerenciador_tarefas.sql contém a estrutura e os dados exportados do banco de dados.

Autoria

Projeto desenvolvido por Larissa, como atividade prática do curso de Desenvolvimento de Sistemas do SENAI.

GitHub: https://github.com/gslarie