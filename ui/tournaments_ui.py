from services import tournament_service
from services.user_service import ADMIN_ROLE
from ui.utils import input_int

def show_tournaments():
    items = tournament_service.get_all_tournaments()
    if not items:
        print("Турниров пока нет")
        return
    for t in items:
        print(f"{t.tournament_id}. {t.name} ({t.sport})")

def tournaments_menu(user):
    is_admin = user.role == ADMIN_ROLE
    while True:
        print("\n===== Турниры =====")
        print("1. Список турниров")
        if is_admin:
            print("2. Добавить турнир")
            print("3. Изменить турнир")
            print("4. Удалить турнир")
        print("0. Назад")
        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                show_tournaments()
            elif choice == "0":
                break
            elif is_admin and choice == "2":
                tournament_service.create_tournament(
                    input("Название: "), input("Вид спорта: ")
                )
                print("Турнир добавлен")
            elif is_admin and choice == "3":
                show_tournaments()
                tournament_service.update_tournament(
                    input_int("ID турнира: "),
                    input("Новое название: "),
                    input("Новый вид спорта: "),
                )
                print("Турнир изменён")
            elif is_admin and choice == "4":
                show_tournaments()
                tournament_service.delete_tournament(input_int("ID турнира: "))
                print("Турнир удалён")
            else:
                print("Неверный пункт меню")
        except Exception as e:
            print(f"Ошибка: {e}")