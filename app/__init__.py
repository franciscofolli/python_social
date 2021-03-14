from flask import Flask
from flask_sqlalchemy import SQLAlchemy #lib de ORM para conversar com um banco de dados através dos MODELS do python
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__) # instanciando Flask no objeto 'app' para execução do projeto

# configurando database com sqlalchemy (lembrar de utilizar metodo atualizado pois o abaixo esta descontinuado)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app) #instanciando nossa aplicação no db 

migrate = Migrate(app, db) # Instanciando migrate que irá cuidar das migrações de banco que recebe 
# minha aplicação (app) e o banco de dados (db) que o mesmo fara as migrações

# migrações é quando acontece alterações no banco de dados, em sua estrutura e derivados, onde 'migramos' o banco

# app instanciado no manager por em seu construtor o mesmo tem o comando de "run server" 
# que é o comando de inicialização do app 
manager = Manager(app) # controle de informações passadas durante a execução 
# cuidará dos comandos realizados para inicializar a execução da aplicação 


manager.add_command('db', MigrateCommand)

# python run.py db init -- irá inicializar o banco de dados, criando a pasta migrations
# python run.py db migrate -- irá criar o storage.db (nomeado na linha 9) e cirar a tabela padrão para ajuda na migração de dados durante a execução do app (chama-se 'alembic versions')
# python run.py db upgrade -- irá realizar as migrações e inserir as novas alterações realizadas no banco de dados

# os comandos db migrate e db update devem ser executados TODA VEZ que houver alterações no banco de dados



from app.controllers import default