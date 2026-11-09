from services.user_service import ADMIN_ROLE
from ui.auth import add_admin
from ui.tournaments_ui import tournaments_menu
from ui.teams_ui import teams_menu
from ui.players_ui import players_menu

def main_menu(user):
    is_admin = user.role == ADMIN_ROLE
    while True:
        role_name = "Администратор" if is_admin else "Пользователь"
        print(f"\n===== {role_name} ({user.username}) =====")
        print("1. Турниры")
        print("2. Команды")
        print("3. Игроки")
        if is_admin:
            print("4. Добавить администратора")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            tournaments_menu(user)
        elif choice == "2":
            teams_menu(user)
        elif choice == "3":
            players_menu(user)
        elif is_admin and choice == "4":
            add_admin()
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню")