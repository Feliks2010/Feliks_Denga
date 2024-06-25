from project.settings import DATABASE
import flask_login
name_fas = None

class User(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String(50), nullable = False)
    password = DATABASE.Column(DATABASE.String(256), nullable = False)
    is_admin = DATABASE.Column(DATABASE.Boolean, nullable = False)

    def __repr__(self) -> str:
        name_fas = self.name
        return f"{self.id, self.name, self.password}"
            
# user = User()
class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key= True)
    name = DATABASE.Column(DATABASE.String(60))
    description = DATABASE.Column(DATABASE.Text)
    count = DATABASE.Column(DATABASE.Integer)
    price = DATABASE.Column(DATABASE.Integer)
    gb = DATABASE.Column(DATABASE.String(10))
    gb1 = DATABASE.Column(DATABASE.String(10))
    start_count = DATABASE.Column(DATABASE.Integer)
    discount = DATABASE.Column(DATABASE.Integer)
    count1 = DATABASE.Column(DATABASE.Integer)

    
    def __repr__(self) -> str:
        return f"name - {self.name}"
    
class Cart(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key= True)
    name_cart = DATABASE.Column(DATABASE.String(60))
    description_cart = DATABASE.Column(DATABASE.Text)
    count_cart = DATABASE.Column(DATABASE.Integer)
    price_cart = DATABASE.Column(DATABASE.Integer)
    gb_cart = DATABASE.Column(DATABASE.String(10))
    gb1_cart = DATABASE.Column(DATABASE.String(10))
    start_count_cart = DATABASE.Column(DATABASE.Integer)
    discount_cart = DATABASE.Column(DATABASE.Integer)
    count1_cart = DATABASE.Column(DATABASE.Integer)
    user_cart = DATABASE.Column(DATABASE.String(60))

    def __repr__(self) -> str:
        return f"name - {self.name}"
