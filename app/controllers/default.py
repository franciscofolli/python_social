from flask import render_template
from app import app

from app.models.forms import LoginForm

# decorator utilizando para definir o nome das rotas
# cada função pode ter mais de um nome de rota, conforme abaixo
@app.route('/')
def index():
    return render_template('index.html')

# é possível realizar a passagem de parametros nas rotas, conforme abaixo
@app.route('/test') # duas rotas para nao obrigar preenchimento de nome na rota
# <int:name> com o int: serve para converter o valor passado para o tipo necessário para sua utilização
@app.route('/test/<name>') # passando parametros na URL
def teste(name=None): # mesmo nome do parametro
    if name:
        return 'Olá, %s!' % name
    else: 
        return 'Olá, Usuário!'

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else: 
        print(form.errors)
    return render_template('login.html',
                            form=form)