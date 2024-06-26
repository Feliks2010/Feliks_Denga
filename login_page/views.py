import flask
from registration_page.models import User
import flask_login
namelog = "axaax"

def show_log_page():
    try:
        if flask.request.method == 'POST':
            log = flask.request.form['name']
            flask.session['log'] = log
            for user in User.query.filter_by(name = flask.request.form["name"]):
                if user.password == flask.request.form["password"]:
                    flask_login.login_user(user)

        if flask_login.current_user.is_authenticated:
            print('hello')
            is_admin = flask_login.current_user.is_admin
            is_name = flask_login.current_user.name
            return flask.redirect(
                        location= "/Authorization/Success_Authorization/"
                    )
        else:
            return flask.render_template(template_name_or_list = "autho.html")

        
    except:
        return "Error"