# Імпортуємо flask_mail
import flask_mail
# Імпортуємо головний додаток
from .settings import project_login
# Задаємо в змінні нашу електронну адресу та пароль
ADMINISTRATION_ADRESS = "artemvaschenko83@gmail.com"
ADMINISTRATION_PASSWORD = "sncj nczy toqt atlm"

# Задаємо сервер
project_login.config["MAIL_SERVER"] = 'smtp.gmail.com'
# Задаємо безпечний порт
project_login.config["MAIL_PORT"] = 587
# Реалізація перевірки пошти в програмах Flask
project_login.config["MAIL_USE_TLS"] = True
# Задаємо нашу пошту та пароль
project_login.config["MAIL_USERNAME"] = ADMINISTRATION_ADRESS
project_login.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD
# Створюємо об'єкт класа Mail
mail = flask_mail.Mail(app=project_login)


