# Імпортуємо необхідні модулі
import flask
from registration_page.models import User
from flask_login import current_user
name = None
# Створюємо функцію для відображення сторінки
def render_success():
    try:
        # Створюємо змiнні для подальшої роботи з html
        is_name = False
        is_authenticated = False
        is_admin = False
        # Cтворюємо умову для перевірки авторизації користувача
        if current_user.is_authenticated:
            # Задаємо у змінній нові значення
            is_admin = current_user.is_admin
            is_authenticated = True
            is_name = current_user
        # Відображаємо сторінку
        return flask.render_template(template_name_or_list = "autho_succes.html", first_name = current_user.name,
                                     is_admin = is_admin, is_authenticated = is_authenticated, is_name = is_name)
    except:
        return "Error"