import flask

success_reg = flask.Blueprint(
    name = "Success",
    import_name = "app",
    template_folder = "success_registration/templates",
    static_folder= "success_registration/static",
    static_url_path="/success_registration/"
)