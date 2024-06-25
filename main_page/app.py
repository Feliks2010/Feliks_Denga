import flask

home = flask.Blueprint(
    name= "home_page",
    import_name= "app",
    template_folder="main_page/templates",
    static_folder="main_page/static",
    static_url_path="/main_page/"
)