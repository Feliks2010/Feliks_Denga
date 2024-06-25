# import telebot

# API_TOKEN = '7456428341:AAGkf0ajHu9vYjYE6rzMO5WV0XnuOU2FFis'
# bot = telebot.TeleBot(API_TOKEN)

# # Обробник для всіх повідомлень
# @bot.message_handler(func=lambda message: True)
# def handle_all_messages(message):
#     if message.chat.type == "supergroup":

#         print(f"Chat ID: {message.chat.id}")
#         print(f"Thread ID: {message.message_thread_id}")
#         bot.reply_to(message, f"Chat ID: {message.chat.id}, Thread ID: {message.message_thread_id}")

# bot.polling()
import telebot
import sqlite3
import os
from registration_page.models import User, Product
from project.settings import project_login, DATABASE

# Ініціалізація бота
bot = telebot.TeleBot("7456428341:AAGkf0ajHu9vYjYE6rzMO5WV0XnuOU2FFis")

# Створення кнопок
button_get_users = telebot.types.InlineKeyboardButton(text="GET USERS", callback_data="get_users")
button_get_products = telebot.types.InlineKeyboardButton(text="GET PRODUCTS", callback_data="get_products")
button_add_product = telebot.types.InlineKeyboardButton(text="ADD PRODUCT", callback_data="add_product")
keyboard = telebot.types.InlineKeyboardMarkup(keyboard=[[button_get_users, button_get_products], [button_add_product]])
button_complete = telebot.types.InlineKeyboardButton(text="ВИКОНАНО", callback_data= "complete")
button_reject = telebot.types.InlineKeyboardButton(text="ВІДХИЛИТИ", callback_data= "reject")
keyboard_cart = telebot.types.InlineKeyboardMarkup(keyboard=[[button_complete, button_reject]])
# Хендлер для команди /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Привіт, користувач", reply_markup=keyboard)

# Хендлер для обробки кнопок
@bot.callback_query_handler(func=lambda call: call.data == "get_users")
def callback_users(call):
    with project_login.app_context():
        users = User.query.all()
        for user in users:
            button_add_admin = telebot.types.InlineKeyboardButton(
                text="GIVE ADMIN", callback_data=f"give_admin_{user.id}")
            button_remove_admin = telebot.types.InlineKeyboardButton(
                text="REMOVE ADMIN", callback_data=f"remove_admin_{user.id}"
            )
            button_remove_user = telebot.types.InlineKeyboardButton(
                text="DELETE USER", callback_data=f"remove_user_{user.id}"
            )
            keyboard_user = telebot.types.InlineKeyboardMarkup(
                [[button_add_admin, button_remove_admin], [button_remove_user]]
            )
            bot.send_message(-1002243362537, f"ID: {user.id}\nName: {user.name}\nPassword:{user.password}\nis_admin: {int(user.is_admin)}", reply_markup=keyboard_user, message_thread_id=2)

@bot.callback_query_handler(func=lambda call: "give_admin_" in call.data)
def callback_give_admin(call):
    user_id = int(call.data.split("_")[2])
    with project_login.app_context():
        user = User.query.get(user_id)
        if user:
            bot.send_message(-1002243362537, f"User {user.name} has gained admin rights!", message_thread_id=2)
            user.is_admin = True
            DATABASE.session.commit()

@bot.callback_query_handler(func=lambda call: "remove_admin_" in call.data)
def callback_remove_admin(call):
    user_id = int(call.data.split("_")[2])
    with project_login.app_context():
        user = User.query.get(user_id)
        if user.is_admin:
            bot.send_message(-1002243362537, f"User {user.name} has lost admin rights!", message_thread_id=2)
            user.is_admin = False
            DATABASE.session.commit()

@bot.callback_query_handler(func=lambda call: "remove_user_" in call.data)
def callback_remove_user(call):
    user_id = int(call.data.split("_")[2])
    with project_login.app_context():
        user = User.query.get(user_id)
        if user:
            bot.send_message(-1002243362537, f"user {user.name} removed successfully!", message_thread_id=2)
            DATABASE.session.delete(user)
            DATABASE.session.commit()

@bot.callback_query_handler(func=lambda call: call.data == "get_products")
def get_products(call):
    with project_login.app_context():
        products = Product.query.all()
        for product in products:
            button_remove_product = telebot.types.InlineKeyboardButton(
                text="DELETE PRODUCT", callback_data=f"remove_product_{product.id}"
            )
            keyboard_product = telebot.types.InlineKeyboardMarkup(
                [[button_remove_product]]
            )
            bot.send_message(-1002243362537, f"ID: {product.id}\nName: {product.name}\nPrice: {product.price}грн\nDiscount: {product.discount}%", message_thread_id=36, reply_markup=keyboard_product)

@bot.callback_query_handler(func=lambda call: "remove_product_" in call.data)
def callback_remove_product(call):
    product_id = int(call.data.split("_")[2])
    with project_login.app_context():
        product = Product.query.get(product_id)
        if product:
            bot.send_message(-1002243362537, f"product {product.name} removed successfully!", message_thread_id=36)

            DATABASE.session.delete(product)
            DATABASE.session.commit()

product = {
    'name': '',
    'price': '',
    'discount': '',
    'description': '',
    'image_url': ''
}
user_step = {}
pro_duct = {}

@bot.callback_query_handler(func=lambda call: call.data == "add_product")
def callback_add_product(call):
    bot.send_message(-1002243362537, "Введіть назву продукту:", message_thread_id=93)
    user_step[-1002243362537] = 'name'

@bot.message_handler(func=lambda message: message.chat.id in user_step)
def handle_message(message):
    global pro_duct
    chat_id = message.chat.id
    text = message.text
    step = user_step[chat_id]

    if step == 'name':
        product['name'] = text
        bot.send_message(chat_id, "Введіть ціну продукту:", message_thread_id=93)
        user_step[chat_id] = 'price'
    elif step == 'price':
        product['price'] = text
        bot.send_message(chat_id, "Введіть знижку на продукт:", message_thread_id=93)
        user_step[chat_id] = 'discount'
    elif step == 'discount':
        product['discount'] = text
        bot.send_message(chat_id, "Введіть опис продукту:", message_thread_id=93)
        user_step[chat_id] = 'description'
    elif step == 'description':
        product['description'] = text
        bot.send_message(chat_id, "Надішліть URL зображення продукту:", message_thread_id=93)
        user_step[chat_id] = 'image_url'
    elif step == 'image_url':
        product['image_url'] = text
        bot.send_message(chat_id, "Дякую! Ваші дані збережено.", message_thread_id=93)
        user_step[chat_id] = 'done'
        with project_login.app_context():
            pro_duct = Product(
                name=product['name'],
                price=product['price'],
                discount=product['discount'],
                description=product['description'],
                start_count=product['image_url']
            )
            DATABASE.session.add(pro_duct)
            DATABASE.session.commit()
