from database.database import init_db
from services import user_service
from ui.auth import login, register_user
from ui.menus import main_menu

def main():
    init_db()
    user_service.ensure_default_admin()

    while True:
        print("\n===== Учёт спортивных соревнований =====")
        print("1. Войти")
        print("2. Регистрация")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            user = login()
            if user:
                main_menu(user)
        elif choice == "2":
            register_user()
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню")

if __name__ == "__main__":
    main()