# Імпорт необхіжний модулей
import flask
from registration_page.models import User
import flask_login
# Створення функції відображення
def show_log_page():
    try:
        # Перевірка, чи отримав сервер метод POST
        if flask.request.method == 'POST':
            # Перевірка, чи існує користувач в базі даних
            for user in User.query.filter_by(name = flask.request.form["name"]):
                # Чи співпадають паролі з бази даних та пароль, який ввела людина в input-кнопку
                if user.password == flask.request.form["password"]:
                    # Авторизація користувача
                    flask_login.login_user(user)
        # Якщо користувач авторизований
        if flask_login.current_user.is_authenticated:
            # Беремо дані з бази даних
            is_admin = flask_login.current_user.is_admin
            is_name = flask_login.current_user.name
            # Виконуємо редірект сторінки за адресою /Authorization/Success_Authorization/
            return flask.redirect(
                        location= "/Authorization/Success_Authorization/"
                    )
        # Якщо користувач не авторизований
        else:
            # Відображення сторінки авторизації
            return flask.render_template(template_name_or_list = "autho.html")

        
    except:
        return "Error"