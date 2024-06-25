import flask_login
from .settings import project_login
from registration_page.models import User

project_login.secret_key = 'KEY'
login_manager = flask_login.LoginManager(app=project_login)
login_manager.login_view = "login"
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)