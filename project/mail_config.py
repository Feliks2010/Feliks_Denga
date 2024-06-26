import flask_mail
from .settings import project_login

ADMINISTRATION_ADRESS = "artemvaschenko83@gmail.com"
ADMINISTRATION_PASSWORD = "sncj nczy toqt atlm"


project_login.config["MAIL_SERVER"] = 'smtp.gmail.com'
project_login.config["MAIL_PORT"] = 587
project_login.config["MAIL_USE_TLS"] = True
project_login.config["MAIL_USERNAME"] = ADMINISTRATION_ADRESS
project_login.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD

mail = flask_mail.Mail(app=project_login)


