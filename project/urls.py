import registration_page, login_page
from .settings import project_login
from main_page import home, render
from success_registration import success_reg, render_success
from success_authorization import success_authp as success_autho,render_success as render_autho
from Shop_page import render_shop, shop_app
from cart_page import cart, render_cart
from admin_page.app import admin
from admin_page.views import render_admin
import admin_main_page


home.add_url_rule(
    rule="/",
    view_func= render
)

success_reg.add_url_rule(
    rule= "/Registration/Success_Registration/",
    view_func=render_success
)
project_login.register_blueprint(
    blueprint= success_reg
)
project_login.register_blueprint(
    blueprint=home
)
registration_page.reg_app.add_url_rule(
    rule = '/Registration/',
    view_func = registration_page.show_reg_page,
    methods = ['GET', 'POST']
)

project_login.register_blueprint(blueprint = registration_page.reg_app)

login_page.log_app.add_url_rule(
    rule = '/Authorization/',
    view_func = login_page.show_log_page,
    methods = ['GET', 'POST']
)

project_login.register_blueprint(blueprint = login_page.log_app)

success_autho.add_url_rule(
    rule= "/Authorization/Success_Authorization/",
    view_func= render_autho
)
project_login.register_blueprint(
    blueprint= success_autho
)

shop_app.add_url_rule(
    rule= "/Shop/",
    view_func= render_shop
)

project_login.register_blueprint(blueprint = shop_app)

cart.add_url_rule(
    rule="/Basket/",
    view_func= render_cart,
    methods = ["POST", "GET"]
)
project_login.register_blueprint(blueprint= cart)

admin.add_url_rule(
    rule="/AdminPage/",
    view_func=render_admin,
    methods= ["GET","POST"]
    )
project_login.register_blueprint(blueprint=admin)

admin_main_page.success_authp.add_url_rule(
    rule="/Admin/",
    view_func= admin_main_page.render_success
)
project_login.register_blueprint(
    blueprint=admin_main_page.success_authp
)