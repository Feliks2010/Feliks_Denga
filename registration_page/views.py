import flask
from .models import User
from project.settings import DATABASE

def show_reg_page():
    try:

        is_registration = False
        if flask.request.method == 'POST':
            user = User(name=flask.request.form['name'],password=flask.request.form['password'], is_admin = False)

            try:
                DATABASE.session.add(user)
                DATABASE.session.commit()
                is_registration = True
            except:
                return 'ERROR'
            return flask.redirect(
                location="Success_Registration/"
            )

        return flask.render_template(template_name_or_list = "register.html")
    except:
        return "Error"
        