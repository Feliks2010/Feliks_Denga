import flask
from registration_page.models import Product
import os
import pandas
def render_cart():
    products = []

    # Перевірка наявності кукі 'product'
    if 'product' in flask.request.cookies:
        id_products = flask.request.cookies.get('product').split(' ')
        ids = []
        for id in id_products:
            if id not in ids:
                count_products = id_products.count(id)
                ids.append(id)
                product = Product.query.get(id)

                if product:
                    product.gb1 = count_products
                    products.append(product)
    # Передача списку товарів у шаблон
    name = flask.session.get('log')
    return flask.render_template(template_name_or_list="cart.html", products=products, first_name = name)