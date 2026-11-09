from services.user_service import authenticate, register, ADMIN_ROLE

def login():
    username = input("Имя пользователя: ")
    password = input("Пароль: ")
    user = authenticate(username, password)
    if not user:
        print("Неверное имя пользователя или пароль")
        return None
    return user

def register_user():
    try:
        register(input("Имя пользователя: "), input("Пароль: "))
        print("Регистрация прошла успешно")
    except Exception as e:
        print(f"Ошибка: {e}")

def add_admin():
    try:
        register(input("Имя нового администратора: "), input("Пароль: "), ADMIN_ROLE)
        print("Администратор добавлен")
    except Exception as e:
        print(f"Ошибка: {e}")