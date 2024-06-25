import flask

success_authp = flask.Blueprint(
    name = "Authorization_Suc",
    import_name = "app",
    template_folder = "success_authorization/templates",
    static_folder= "success_authorization/static",
    static_url_path="/success_authorization/"
)