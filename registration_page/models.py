from project.settings import DATABASE
import flask_login
name_fas = None
# Створення моделі User
class User(DATABASE.Model, flask_login.UserMixin):
    # Створюємо унікальний стовбець
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    # Створюємо стовбець для імені
    name = DATABASE.Column(DATABASE.String(50), nullable = False)
    # Створюємо стовбець для паролю
    password = DATABASE.Column(DATABASE.String(256), nullable = False)
    # Створюємо стовбець для перевірки адміна
    is_admin = DATABASE.Column(DATABASE.Boolean, nullable = False)
    # Створюємо функцію для виводу ім'я та пароля на екран
    def __repr__(self) -> str:
        return f"{self.id, self.name, self.password}"
            
# Створюємо модель Product
class Product(DATABASE.Model):
    # Створюємо унікальний стовбець
    id = DATABASE.Column(DATABASE.Integer, primary_key= True)
    # Створюємо стовбець для імені
    name = DATABASE.Column(DATABASE.String(60))
    # Створюємо стовбець для опису
    description = DATABASE.Column(DATABASE.Text)
    # Створюємо стовбець для кількості
    count = DATABASE.Column(DATABASE.Integer)
    # Створюємо стовбець для ціни
    price = DATABASE.Column(DATABASE.Integer)
    # Створюємо стовбець для об'єму пам'яті
    gb = DATABASE.Column(DATABASE.String(10))
    # Створюємо стовбець для об'єму пам'яті
    gb1 = DATABASE.Column(DATABASE.String(10))
    # Створюємо стовбець для початкової кількості
    start_count = DATABASE.Column(DATABASE.Integer)
    # Створюємо стовбець для знижки
    discount = DATABASE.Column(DATABASE.Integer)
    # Створюємо стовбець для кількості
    count1 = DATABASE.Column(DATABASE.Integer)

    # Створюємо функцію для виводу ім'я
    def __repr__(self) -> str:
        return f"name - {self.name}"
# Створюємо модель Cart
class Cart(DATABASE.Model):
    # Створюємо унікальний стовбець
    id = DATABASE.Column(DATABASE.Integer, primary_key= True)
    # Створюємо стовбець для імені
    name_cart = DATABASE.Column(DATABASE.String(60))
    # Створюємо стовбець для опису
    description_cart = DATABASE.Column(DATABASE.Text)
    # Створюємо стовбець для кількості
    count_cart = DATABASE.Column(DATABASE.Integer)
    # Створюємо стовбець для ціни
    price_cart = DATABASE.Column(DATABASE.Integer)
    # Створюємо стовбець для об'єму пам'яті
    gb_cart = DATABASE.Column(DATABASE.String(10))
    # Створюємо стовбець для об єму пам'яті
    gb1_cart = DATABASE.Column(DATABASE.String(10))
    # Створюємо стовбець для початкової кількості
    start_count_cart = DATABASE.Column(DATABASE.Integer)
    # Створюємо стовбець для знижки
    discount_cart = DATABASE.Column(DATABASE.Integer)
    # Створюємо стовбець для кількості
    count1_cart = DATABASE.Column(DATABASE.Integer)
    # Створюємо стовбець для користувача, який замовив
    user_cart = DATABASE.Column(DATABASE.String(60))
    # Створюємо функцію для виводу ім'я
    def __repr__(self) -> str:
        return f"name - {self.name}"
