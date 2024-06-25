import flask

def render_success():
    return flask.render_template(template_name_or_list = "registr.html")