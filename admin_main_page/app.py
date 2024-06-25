import flask

success_authp = flask.Blueprint(
    name = "admin_main",
    import_name = "app",
    template_folder = "admin_main_page/templates",
    static_folder= "admin_main_page/static",
    static_url_path="/admin_main/"
)