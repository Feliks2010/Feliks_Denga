import flask

home = flask.Blueprint(
    name = "home_page",
    import_name = "app",
    template_folder = "Home_page/templates",
    static_folder= "Home_page/static",
    static_url_path="/home/"
)