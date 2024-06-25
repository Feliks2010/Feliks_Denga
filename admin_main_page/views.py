import flask
from registration_page.models import User
import flask_login
name = None

def render_success():
    name = flask.session.get('log')
    return flask.render_template(template_name_or_list = "admin_main.html", first_name = name)