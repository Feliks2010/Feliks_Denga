import flask
import os
import pandas
from registration_page.models import Product
from project.settings import DATABASE
from flask_login import current_user
import telebot
from bot_app.main import bot, pro_duct
# Ініціалізація бота (якщо це необхідно, в залежності від вашої структури проекту)
# bot = telebot.TeleBot("your_bot_token_here")

# Функція для відображення сторінки магазину
def render_shop():
    if len(list(Product.query.all())) == 0:
        excel_path = os.path.abspath(__file__ + "/../static/Product.xlsx")
        data_excel = pandas.read_excel(io=excel_path, header=None, names=["name", "description", "count", "price", "path", "gb1", "start_count", "discount"])
        
        for row in data_excel.iterrows():
            row_data = row[1]
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
            DATABASE.session.add(product)
        
        DATABASE.session.commit()
    
    # Додайте надсилання повідомлення боту після коміту продукту
    
    is_admin = False
    
    if current_user.is_authenticated:
        is_admin = current_user.is_admin
        print("adas")

    return flask.render_template(
        template_name_or_list="shop_app.html",
        products=Product.query.all(),
        first_name=current_user.name,
        is_admin=is_admin
    )
