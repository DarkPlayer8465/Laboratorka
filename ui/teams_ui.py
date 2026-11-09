from services import team_service, tournament_service
from services.user_service import ADMIN_ROLE
from ui.utils import input_int

def print_teams(teams):
    if not teams:
        print("Команд пока нет")
        return
    for t in teams:
        print(f"{t.team_id}. {t.name} — турнир: {t.tournament_name}")

def _show_tournaments():
    for t in tournament_service.get_all_tournaments():
        print(f"{t.tournament_id}. {t.name} ({t.sport})")

def teams_menu(user):
    is_admin = user.role == ADMIN_ROLE
    while True:
        print("\n===== Команды =====")
        print("1. Все команды")
        print("2. Команды турнира")
        if is_admin:
            print("3. Добавить команду")
            print("4. Изменить команду")
            print("5. Удалить команду")
        print("0. Назад")
        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                print_teams(team_service.get_all_teams())
            elif choice == "2":
                _show_tournaments()
                print_teams(
                    team_service.get_teams_by_tournament(input_int("ID турнира: "))
                )
            elif choice == "0":
                break
            elif is_admin and choice == "3":
                _show_tournaments()
                team_service.create_team(
                    input("Название команды: "), input_int("ID турнира: ")
                )
                print("Команда добавлена")
            elif is_admin and choice == "4":
                print_teams(team_service.get_all_teams())
                team_service.update_team(
                    input_int("ID команды: "),
                    input("Новое название: "),
                    input_int("ID турнира: "),
                )
                print("Команда изменена")
            elif is_admin and choice == "5":
                print_teams(team_service.get_all_teams())
                team_service.delete_team(input_int("ID команды: "))
                print("Команда удалена")
            else:
                print("Неверный пункт меню")
        except Exception as e:
            print(f"Ошибка: {e}")