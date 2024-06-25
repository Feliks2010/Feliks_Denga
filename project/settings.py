import flask
import os
import flask_sqlalchemy
import flask_migrate

# Ініціалізація Flask-додатку
project_login = flask.Flask(
    import_name="settings",
    instance_path=os.path.abspath(__file__ + "/.."),
    template_folder='project/templates'
)

# Налаштування бази даних
project_login.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Ініціалізація SQLAlchemy
DATABASE = flask_sqlalchemy.SQLAlchemy(app=project_login)

# Ініціалізація Flask-Migrate для керування міграціями
MIGRATE = flask_migrate.Migrate(app=project_login, db=DATABASE)

# Створення таблиць у базі даних, якщо вони ще не створені
with project_login.app_context():
    DATABASE.create_all()
