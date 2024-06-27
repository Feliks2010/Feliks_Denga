# Імпортування необхідних модулей
import flask
from .models import User
from project.settings import DATABASE
# Створюємо функцію для відображення сторінки
def show_reg_page():
    try:
        # Перевірка, чи отримали метод POST
        if flask.request.method == 'POST':
            # Створення об'єкта користувача, в якого записується його дані, які він ввів в input-кнопки
            user = User(name=flask.request.form['name'],password=flask.request.form['password'], is_admin = False)

            try:
                # Додавання користувача в базу даних
                DATABASE.session.add(user)
                # Збереження змін
                DATABASE.session.commit()
            except:
                return 'ERROR'
            # Виконується перехід сторінки за адресою "Success_Registration/"
            return flask.redirect(
                location="Success_Registration/"
            )
        # Відображення сторінки
        return flask.render_template(template_name_or_list = "register.html")
    except:
        return "Error"
        