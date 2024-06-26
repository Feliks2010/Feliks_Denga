import flask
from registration_page.models import Product,Cart
import os
from flask_login import current_user
import pandas
import telebot
from bot_app.main import bot, keyboard_cart
from project.settings import DATABASE
from project.mail_config import mail,ADMINISTRATION_ADRESS
from flask_mail import Message
# from bot_app.main import bot
# Створюємо функцію для відображення
def render_cart():
    try:
        # Створюємо пустий список
        products = []

        # Перевірка наявності кукі 'product'
        if 'product' in flask.request.cookies:
            # Беремо з кукі значеня
            id_products = flask.request.cookies.get('product').split(' ')
            # Створюємо пустий список для id
            ids = []
            # Перебираємо наші id
            for id in id_products:
                # Якщо id немаєх в списку ids
                if id not in ids:
                    # Знаходимо кількість однакових значень id в списку id_products
                    count_products = id_products.count(id)
                    # Записуємо id в список ids
                    ids.append(id)
                    # Знаходимо товар по id
                    product = Product.query.get(id)
                    # Якщо продукт створений
                    if product:

                        # Записуємо кількість однакових значень в поле gb1 товару
                        product.gb1 = count_products
                        # Записуємо товар в список товарів
                        products.append(product)
                        if flask.request.method == 'POST':
                            
                            name = flask.request.form["name"]
                            surname = flask.request.form["surname"]
                            phone = flask.request.form["phone"]
                            email = flask.request.form["email"]
                            city = flask.request.form["city"]
                            department = flask.request.form["department"]
                            wish = flask.request.form["wish"]
                            product_name = product.name
                            product_price = product.price
                            product_discount = product.discount
                            product_cart = Cart(
                                            name_cart = product_name,
                                            price_cart = int(product_price - (product_price * product_discount) / 100),
                                            discount_cart = product_discount,
                                            count_cart = count_products,
                                            user_cart = name,
                                            )
                            DATABASE.session.add(product_cart)
                            DATABASE.session.commit()
                            print(products)
                            message_text = ""
                            for product in products:
                                message_text += f"Надійшло замовлення від {name} {surname}!\nІм'я товару: {product.name}\nЦіна: {product.price} \nЗнижка: {product.discount}\nНомер телефона: {phone}\nЕлектронна адреса: {email} \nМісто: {city}\nДодаткові побажання: {wish}"
                            message = Message(
                                "message order",
                                sender= ADMINISTRATION_ADRESS,
                                recipients=['artemvashenko201010@gmail.com'],
                                body = message_text
                                            
                            )
                            mail.send(message)
                            count = 0
                            if count == 0:
                                bot.send_message(-1002243362537, f"Надійшло замовлення від {name} {surname}! \nНомер телефона: {phone}\nПошта: {email}\nМісто: {city}\nВідділеня: {department}\nПобажання: {wish}",message_thread_id=40) 
                            count += 1
                            product_cart_id = Cart.query.get(id)
                            
                            bot.send_message(-1002243362537, f"\nНазва продукту: {product_cart_id.name_cart}\nЦіна: {product_cart_id.price_cart}\nЗнижка: {product_cart_id.discount_cart}\nКількість:{product_cart_id.count_cart}",message_thread_id=40, reply_markup= keyboard_cart)
        # Створюємо змінну для подальшої роботи з html
        is_admin = False
        # Створюємо умову для перевірки авторизації користувача
        if current_user.is_authenticated:
            # Задаємо змінній нове значення
            is_admin = current_user.is_admin
        # Відображаємо сторінку
        
            
        return flask.render_template(template_name_or_list="cart.html", products=products, first_name = current_user.name, is_admin = is_admin)
    except:
        return "Error"    