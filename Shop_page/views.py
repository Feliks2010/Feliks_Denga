# Іморт усіх необхідних модулей та об'єктів
import flask
import os
import pandas
from registration_page.models import Product
from project.settings import DATABASE
from flask_login import current_user
import telebot
from bot_app.main import bot, pro_duct

# Функція для відображення сторінки магазину
def render_shop():
    try:
        # Якщо продуктів немає
        if len(list(Product.query.all())) == 0:
            # Створення деректорії за якою храниться таблиця excel
            excel_path = os.path.abspath(__file__ + "/../static/Product.xlsx")
            # Зчитування даних з таблиці
            data_excel = pandas.read_excel(io=excel_path, header=None, names=["name", "description", "count",
                                                             "price", "path", "gb1", "start_count", "discount"])
            # Перебираємо дані в рядок
            for row in data_excel.iterrows():
                # Перебираємо дані в рядку
                row_data = row[1]
                # Створення об'єкту продукту
                product = Product(
                    name=row_data['name'],
                    description=row_data['description'],
                    count=row_data['count'],
                    price=row_data['price'],
                    gb=row_data['path'],
                    gb1=row_data['gb1'],
                    start_count=row_data['start_count'],
                    discount=row_data['discount']
                )
                # Додавання продукту до бази даних
                DATABASE.session.add(product)
            # Збереження змін
            DATABASE.session.commit()
        
        # Перезапис змінної
        is_admin = False
        # Перевірка на авторизацію користувача
        if current_user.is_authenticated:
            # Перезапис змінної
            is_admin = current_user.is_admin
        # Відображаємо сторінку
        return flask.render_template(
            template_name_or_list="shop_app.html",
            products=Product.query.all(),
            first_name=current_user.name,
            is_admin=is_admin
        )
    except:
        return "Error"