from flask import Flask
from flask_sqlalchemy import SQLAlchemy #lib de ORM para conversar com um banco de dados através dos MODELS do python

app = Flask(__name__)
# configurando database com sqlalchemy (lembrar de utilizar metodo atualizado pois o abaixo esta descontinuado)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app) #instanciando nossa aplicação no db 
 
from app.controllers import default