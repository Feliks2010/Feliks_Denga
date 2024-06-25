import flask 

log_app = flask.Blueprint(
    name= "authorization",
    import_name= "login_page",
    template_folder = "templates",
    static_folder= "static",
    static_url_path="/login_page/"
)