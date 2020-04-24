import os 
from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager, current_user
from functools import wraps

###################################################
################ Aplicação Flask ##################
###################################################

app = Flask(__name__)

app.config['secrect_key'] = "mysecretkey"

###################################################
################ Banco de Dados ###################
###################################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

###################################################
################ Login ############################
###################################################

login_mananger = LoginManager()
login_mananger.init_app(app)
# login_mananger.login_view = "usuarios.login"

def login_required(role=["ANY"]):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):

            if not current_user.is_authenticated:
               return current_app.login_manager.unauthorized()
            urole = current_user.get_urole()
            if ( (urole not in role) and (role != ["ANY"])):
                return current_app.login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

###################################################
################ Blueprints #######################
###################################################

from busca_assincrona.usuarios.views import usuarios

app.register_blueprint(usuarios,url_prefix="/usuarios")


@app.route("/")
def index():
    return "Olá, mundo!"
