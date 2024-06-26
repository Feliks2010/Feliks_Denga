import flask
import os
from registration_page.models import Product
from project.settings import DATABASE
from flask_login import current_user

def render_admin():
    try:
        products = Product.query.all()
        if flask.request.method == "POST":
                    
            if flask.request.form.get('del'):
                product_id = int(flask.request.form['del'])
                product_del = Product.query.get(product_id)
                
                
                if product_del:
                    DATABASE.session.delete(product_del)
                    DATABASE.session.commit()
                    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../../shop_page/static/images/{product_del.name}.png")
                    if os.path.exists(image_path):
                        os.remove(image_path)
            elif flask.request.form.get('name'):
                name = flask.request.form['name']
                description = flask.request.form['description']
                price = float(flask.request.form['price'])
                count = int(flask.request.form['count1'])
                discount = int(flask.request.form['discount'])
                    
                    
                    
                product = Product(
                        name=name,
                        description="256gb",
                        price=price,
                        count=count,
                        discount=discount,
                        gb= "512 Гб",
                        gb1= "1 Тб"
                    )
                DATABASE.session.add(product)
                DATABASE.session.commit()
                image_file = flask.request.files['image']
                image_path = os.path.abspath(__file__+ '/../../Shop_page/static/images/'+ f'{product.name}.png') 
                print(image_path)
                # os.makedirs(os.path.dirname(image_path), exist_ok=True)
                image_file.save(image_path)
            else:
                    
                    list_data = flask.request.form['submit-change'].split('-')
                    print(list_data)
                    product = Product.query.get(int(list_data[1]))
                    path = os.path.abspath(__file__ + f"/../../Shop_page/static/images/{product.name}.png")
                    if "image" == list_data[0]:
                        os.remove(path)
                        img = flask.request.files["image"]
                        img.save(path)
                    elif "name" == list_data[0]:
                        print(flask.request.form)
                        product_name = flask.request.form['text']
                        path2 = os.path.abspath(__file__ + f"/../../Shop_page/static/images/{product_name}.png")
                        os.rename(path,  path2)
                        product.name =  product_name
                        DATABASE.session.commit()
                    elif "price" == list_data[0]:
                        product_price = flask.request.form['text']
                        product.price = product_price
                        DATABASE.session.commit()
                    elif "discount" == list_data[0]:
                        product_discount = flask.request.form['text']
                        product.discount = product_discount
                        DATABASE.session.commit()
                    elif "gb" == list_data[0]:
                        product_gb = flask.request.form['text']
                        product.description = product_gb
                        DATABASE.session.commit()
                    elif "gb1" == list_data[0]:
                        product_gb1 = flask.request.form['text']
                        product.gb = product_gb1
                        DATABASE.session.commit()
                    elif "gb2" == list_data[0]:
                        product_gb2 = flask.request.form['text']
                        product.gb1 = product_gb2
                        DATABASE.session.commit()
        is_admin = False
        if current_user.is_authenticated:
            is_admin = current_user.is_admin
            
        if is_admin ==True:
            return flask.render_template("admin_page.html", products = products, first_name = current_user.name, is_admin = is_admin)
        
        else:
            return flask.redirect("/Authorization/Success_Authorization/")

    except:
        return "Error"