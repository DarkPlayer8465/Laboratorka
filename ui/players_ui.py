from services import player_service, team_service
from services.user_service import ADMIN_ROLE
from ui.utils import input_int

def print_players(players):
    if not players:
        print("Игроков пока нет")
        return
    for p in players:
        print(
            f"{p.player_id}. {p.name} — {p.position}, "
            f"команда: {p.team_name}, турнир: {p.tournament_name}"
        )

def _show_teams():
    for t in team_service.get_all_teams():
        print(f"{t.team_id}. {t.name} — турнир: {t.tournament_name}")

def players_menu(user):
    is_admin = user.role == ADMIN_ROLE
    while True:
        print("\n===== Игроки =====")
        print("1. Все игроки")
        print("2. Состав команды")
        if is_admin:
            print("3. Добавить игрока")
            print("4. Изменить игрока")
            print("5. Удалить игрока")
        print("0. Назад")
        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                print_players(player_service.get_all_players())
            elif choice == "2":
                _show_teams()
                print_players(
                    player_service.get_players_by_team(input_int("ID команды: "))
                )
            elif choice == "0":
                break
            elif is_admin and choice == "3":
                _show_teams()
                player_service.create_player(
                    input("Имя игрока: "),
                    input("Позиция: "),
                    input_int("ID команды: "),
                )
                print("Игрок добавлен")
            elif is_admin and choice == "4":
                print_players(player_service.get_all_players())
                player_service.update_player(
                    input_int("ID игрока: "),
                    input("Новое имя: "),
                    input("Новая позиция: "),
                    input_int("ID команды: "),
                )
                print("Игрок изменён")
            elif is_admin and choice == "5":
                print_players(player_service.get_all_players())
                player_service.delete_player(input_int("ID игрока: "))
                print("Игрок удалён")
            else:
                print("Неверный пункт меню")
        except Exception as e:
            print(f"Ошибка: {e}")