import flask
import flask_login
from registration_page.models import Product
def render():
    return flask.render_template(template_name_or_list= "home.html", login_page = flask_login,         pro_ducts= Product.query.all())