from busca_assincrona import app, db, login_mananger, login_required
from flask import Blueprint, render_template, redirect, flash, request, url_for
from flask_login import current_user, login_user, logout_user
from flask_bcrypt import Bcrypt

# Blueprint
usuarios = Blueprint('usuarios',__name__,template_folder='templates')


