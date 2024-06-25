import flask

shop_app = flask.Blueprint(
    name = "shop_app",
    import_name = "app",
    template_folder = "Shop_page/templates",
    static_folder = "Shop_page/static",
    static_url_path = "/Shop_page/"
)