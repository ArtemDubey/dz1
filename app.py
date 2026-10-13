def show_menu(dishes):
    print("\n--- МЕНЮ ---")
    for i, dish in enumerate(dishes, 1):
        print(f"{i}. {dish['name']} - {dish['price']} грн ({dish['type']})")
def add_dish(dishes):
    name = input("Введіть назву нової страви: ")
    while True:
        try:
            price = float(input("Введіть ціну (більше 0): "))
            if price > 0:
                break
            print("Ціна має бути більшою за 0!")
        except ValueError:
            print("Будь ласка, введіть число.")
    dish_type = input("Введіть тип страви (наприклад, main, drink, dessert): ")
    dishes.append({"name": name, "price": price, "type": dish_type})
    print(f"Страву '{name}' успішно додано!")
def show_tables(tables):
    print("\n--- СТОЛИКИ ---")
    for t in tables:
        status = "Зайнятий" if t["is_busy"] else "Вільний"
        print(f"Столик №{t['number']} (Місць: {t['seats']}) — Статус: {status}")
def seat_guests(tables):
    try:
        guests_count = int(input("Введіть кількість гостей: "))
    except ValueError:
        print("Помилка вводу. Введіть ціле число.")
        return None
    for t in tables:
        if not t["is_busy"] and t["seats"] >= guests_count:
            t["is_busy"] = True
            print(f"Гостей посаджено за столик №{t['number']}.")
            return t
    print("Місць немає.")
    return None
def take_order(dishes, table):
    if not table:
        print("Спочатку потрібно посадити гостей за столик!")
        return []
    show_menu(dishes)
    order = []
    print("Вводьте номери страв для замовлення. Введіть 0 для завершення.")
    while True:
        try:
            choice = int(input("Номер страви (0 для виходу): "))
            if choice == 0:
                break
            if 1 <= choice <= len(dishes):
                order.append(dishes[choice - 1])
                print(f"Додано: {dishes[choice - 1]['name']}")
            else:
                print("Невірний номер страви.")
        except ValueError:
            print("Будь ласка, введіть число.")
    return order
def calc_total(order):
    total = sum(dish["price"] for dish in order)
    if total > 2000:
        total *= 0.9
        print("Застосовано знижку 10%!")
    elif total > 1000:
        total *= 0.95
        print("Застосовано знижку 5%!")
    return total
def free_table(table):
    if table:
        table["is_busy"] = False
        print(f"Столик №{table['number']} звільнено.")
def main():
    dishes = [
        {"name": "Борщ", "price": 120, "type": "main"},
        {"name": "Узвар", "price": 40, "type": "drink"},
        {"name": "Медовик", "price": 90, "type": "dessert"},
        {"name": "Вареники", "price": 100, "type": "main"},
        {"name": "Салат", "price": 80, "type": "main"},
        {"name": "Сік", "price": 50, "type": "drink"},
    ]
    tables = [
        {"number": 1, "seats": 2, "is_busy": False},
        {"number": 2, "seats": 4, "is_busy": False},
        {"number": 3, "seats": 4, "is_busy": False},
        {"number": 4, "seats": 6, "is_busy": False},
    ]
    served_tables_count = 0
    total_revenue = 0.0
    current_table = None
    while True:
        print("\nЕСТОРАН «СМАКОТА»")
        print("1. Показати меню")
        print("2. Додати страву")
        print("3. Показати столики")
        print("4. Посадити гостей")
        print("5. Прийняти замовлення")
        print("6. Закрити зміну")
        print("0. Вихід")
        choice = input("Оберіть дію: ")
        if choice == "1":
            show_menu(dishes)
        elif choice == "2":
            add_dish(dishes)
        elif choice == "3":
            show_tables(tables)
        elif choice == "4":
            current_table = seat_guests(tables)
        elif choice == "5":
            order = take_order(dishes, current_table)
            if order:
                total = calc_total(order)
                print(f"\nЧЕК")
                for item in order:
                    print(f"- {item['name']}: {item['price']} грн")
                print(f"Сума до сплати: {total:.2f} грн")
                total_revenue += total
                served_tables_count += 1
                free_table(current_table)
                current_table = None
        elif choice == "6":
            print("\nЗАКРИТТЯ ЗМІНИ")
            print(f"Кількість обслугованих столиків: {served_tables_count}")
            print(f"Загальна виручка: {total_revenue:.2f} грн")
            break
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір!")
if __name__ == "__main__":
    main() #більшість коду старався робити сам, але частину в пайтоні уже призабув і трохи користувався ШІ і загалом інтернетом