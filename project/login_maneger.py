# Імпортування flask_login
import flask_login
# Імпортуємо наш головний додаток
from .settings import project_login
# Імпортуємо модель User
from registration_page.models import User
# Задаємо secret_key
project_login.secret_key = 'KEY'
# Створюємо об'єкт класа LoginManager
login_manager = flask_login.LoginManager(app=project_login)
# Задаємо ім'я входу в систему
login_manager.login_view = "login"
# Створюємо функцію, яка загружає користувача
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)