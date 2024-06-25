import flask 

cart = flask.Blueprint(
    name= "cart",
    import_name= "app",
    template_folder= "cart_page/templates/",
    static_folder= "cart_page/static",
    static_url_path="/cart_page/"
)