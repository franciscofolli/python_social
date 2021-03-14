from app import db

class User(db.Model): #herdar classe de modelo padrão de database
    __tablename__ = 'users' # cirar nomes de tabelas no plural (boa pratica)

    # identificação de registro (PK, auto incremental, inteiro)
    # db.Column(<tipo de dado>, <chave primaria True or False>)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String(60))
    email = db.Column(db.String(60), unique=True)

    def __init__ (self, username, password, name, email): # na criação do construtor são informados os campos obrigatorios
        self.username = username
        self.password = password
        self.name = name 
        self.email = email

    def __repr__(self): #abreviação de representação - traz resposta de pesquisa no banco de dados
        return '<User %r>' % self.username

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) #criação de chave estrangeira

    user = db.relationship('User', foreign_keys=user_id) # relacionamento com a tabela User para trazer todas as informações do usuário que tiver postado

    def __init__ (self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % self.id

class Follow(db.Model):
    __tablename__ = 'follow'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id) # relacionamento
    follower = db.relationship('User', foreign_keys=follower_id) # relacionamento