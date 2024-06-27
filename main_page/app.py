# Імпортуємо бібліотеку flask
import flask
# Створюємо об'єкт з класом Blueprint
home = flask.Blueprint(
    # Задаємо нашому додатку ім'я
    name= "home_page",
    # Вказуємо ім'я модуля в якому він знаходиться
    import_name= "app",
    # Вказуємо шлях до папки з файлом html
    template_folder="main_page/templates",
    # Вказуємо шлях до папки з статичними файлaми
    static_folder="main_page/static",
    # Встановлюємо URL шлях доступу до статичних файлів цього додатку
    static_url_path="/main_page/"
)