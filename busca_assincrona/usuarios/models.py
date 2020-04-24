from busca_assincrona import db
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

# Model de usuário

class User(db.Model,UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, _name, _password, _email):
        self.name = _name
        self.password = _password
        self.email = _email
    
    def check_senha(self, _password):
        bcrypt = Bcrypt()
        return bcrypt.check_password_hash(self.password,_password)