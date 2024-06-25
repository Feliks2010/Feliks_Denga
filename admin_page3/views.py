import flask, os
from registration_page.models import Product
from project.settings import DATABASE

def render_admin():
    if flask.request.method == 'POST':
        try:
            if flask.request.form.get('del') == None:
                product = Product(
                    name = flask.request.form['name'],
                    description = flask.request.form['description'],
                    price = flask.request.form['price'],
                    count = flask.request.form['count1'],
                    discount = flask.request.form['discount']
                )
                DATABASE.session.add(product)
                DATABASE.session.commit()

                image_file = flask.request.files['image']
                image_file.save(os.path.abspath(__file__ + f'/../../shop_page/static/images/{product.name}.png'))
            else:
                product_id = int(flask.request.form['del'])
                product_del = Product.query.get(product_id)
                if Product.query.get(product_id):
                    DATABASE.session.delete(product_del)
                    DATABASE.session.commit()
                    os.remove(os.path.abspath(__file__ + f"/../../shop_page/static/images/{product_del.name}.png"))
        except Exception as e:
            print(e)

    return flask.render_template(template_name_or_list = 'admin.html', products = Product.query.all())