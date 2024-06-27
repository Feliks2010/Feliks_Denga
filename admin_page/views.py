# Імпортування модулей
import flask
import os
from registration_page.models import Product
from project.settings import DATABASE
from flask_login import current_user
# Створення функції для відображення сторінки
def render_admin():
    try:
        # Створюємо список з продуктів
        products = Product.query.all()
        # Якщо сервер отримав метод POST
        if flask.request.method == "POST":
            # Якщо в формі присутня кнопка з іменем del
            if flask.request.form.get('del'):
                # Шукаємо id кнопки
                product_id = int(flask.request.form['del'])
                # Знаходимо товар за id кнопки
                product_del = Product.query.get(product_id)
                # Якщо продукт існує
                if product_del:
                    # Видаляємо продукт
                    DATABASE.session.delete(product_del)
                    # Зберігаємо оновлення
                    DATABASE.session.commit()
                    # Створюємо шлях до картинки
                    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../../shop_page/static/images/{product_del.name}.png")
                    # Якщо шлях створений
                    if os.path.exists(image_path):
                        # Видаляємо картинку
                        os.remove(image_path)
            # Якщо в формі присутня кнопка з іменем name
            elif flask.request.form.get('name'):
                # Знаходимо дані
                name = flask.request.form['name']
                description = flask.request.form['description']
                price = float(flask.request.form['price'])
                count = int(flask.request.form['count1'])
                discount = int(flask.request.form['discount'])
                # За цими даними створюємо продукт
                product = Product(
                        name=name,
                        description="256gb",
                        price=price,
                        count=count,
                        discount=discount,
                        gb= "512 Гб",
                        gb1= "1 Тб"
                    )
                # Додаємо продукт до бази даних
                DATABASE.session.add(product)
                # Зберігаємо оновлення
                DATABASE.session.commit()
                # Створюємо шлях до картинки
                image_file = flask.request.files['image']
                image_path = os.path.abspath(__file__+ '/../../Shop_page/static/images/'+ f'{product.name}.png') 
                # Зберігаємо картинку
                image_file.save(image_path)
            else:
                    # Знаходимо id
                    list_data = flask.request.form['submit-change'].split('-')
                    # Знаходимо товар по id
                    product = Product.query.get(int(list_data[1]))
                    # Створюємо шлях до папки
                    path = os.path.abspath(__file__ + f"/../../Shop_page/static/images/{product.name}.png")
                    # Якщо змінюється картинка
                    if "image" == list_data[0]:
                        # Видаляємо стару картинку
                        os.remove(path)
                        # Зберігаємо нову картинку
                        img = flask.request.files["image"]
                        img.save(path)
                    # Якщо змінюється ім'я
                    elif "name" == list_data[0]:
                        # Знаходимо текст
                        product_name = flask.request.form['text']
                        # Знаходимо шлях до картинки та змінюємо назву картинки
                        path2 = os.path.abspath(__file__ + f"/../../Shop_page/static/images/{product_name}.png")
                        os.rename(path,  path2)
                        # Змінюємо дані в базі даних
                        product.name =  product_name
                        # Зберігаємо зміни
                        DATABASE.session.commit()
                    # Якщо змінюється ціна
                    elif "price" == list_data[0]:
                        # Дізнаємося нову ціну
                        product_price = flask.request.form['text']
                        # Змінюємо ціну в базі даних
                        product.price = product_price
                        # Зберігаємо зміни
                        DATABASE.session.commit()
                    # Якщо змінюється знижка
                    elif "discount" == list_data[0]:
                        # Дізнаємося нову знижку
                        product_discount = flask.request.form['text']
                        # Змінюємо знижку в базі даних
                        product.discount = product_discount
                        # Зберігаємо зміни
                        DATABASE.session.commit()
                    # Якщо змінюється об'єм пам'яті
                    elif "gb" == list_data[0]:
                        # Дізнаємося новий об'єм
                        product_gb = flask.request.form['text']
                        # Перезаписуємо дані
                        product.description = product_gb
                        # Зберігаємо зміни
                        DATABASE.session.commit()
                    # Якщо змінюється об'єм пам'яті
                    elif "gb1" == list_data[0]:
                        # Дізнаємося новий об'єм
                        product_gb1 = flask.request.form['text']
                        # Перезаписуємо об'єм
                        product.gb = product_gb1
                        # Зберігаємо зміни
                        DATABASE.session.commit()
                    # Якщо змінюється об'єм пам'яті
                    elif "gb2" == list_data[0]:
                        # Дізнаємося новий об'єм
                        product_gb2 = flask.request.form['text']
                        # Перезаписуємо дані
                        product.gb1 = product_gb2
                        # Зберігаємо зміни
                        DATABASE.session.commit()
        is_admin = False
        # Якщо користувач авторизований
        if current_user.is_authenticated:
            is_admin = current_user.is_admin
            
        if is_admin ==True:
            return flask.render_template("admin_page.html", products = products, first_name = current_user.name, is_admin = is_admin)
        
        else:
            return flask.redirect("/Authorization/Success_Authorization/")

    except:
        return "Error"