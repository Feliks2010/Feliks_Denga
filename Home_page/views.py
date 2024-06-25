import flask
from registration_page.models import Product

def render():
    return flask.render_template(
        template_name_or_list = "home.html",
        pro_ducts= Product.query.all()
    )