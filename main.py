"""Учёт расходов — консольная программа с итогами по категориям."""
from dataclasses import dataclass


@dataclass
class Expense:
    category: str
    amount: float


def parse_amount(text):
    """Превращает ввод в положительное число. Если не получилось — None."""
    try:
        amount = float(text.strip().replace(",", "."))
    except ValueError:
        return None
    if not (0 < amount < 1000000000):
        return None
    return amount


def add_expense(expenses, category, amount):
    """Добавляет трату в список. Возвращает True, если успешно."""
    category = category.strip().lower()
    if category == "" or amount is None:
        return False
    expenses.append(Expense(category, amount))
    return True


def totals_by_category(expenses):
    """Считает сумму трат по каждой категории: {категория: сумма}."""
    totals = {}
    for item in expenses:
        if item.category in totals:
            totals[item.category] = totals[item.category] + item.amount
        else:
            totals[item.category] = item.amount
    return totals


def show_report(expenses):
    """Печатает отчёт: суммы по категориям, общий итог и главную категорию."""
    if len(expenses) == 0:
        print("Трат пока нет.")
        return
    totals = totals_by_category(expenses)
    all_sum = 0
    top_category = ""
    top_sum = 0
    print("\n--- Отчёт ---")
    for category in totals:
        print(category, "-", totals[category])
        all_sum = all_sum + totals[category]
        if totals[category] > top_sum:
            top_sum = totals[category]
            top_category = category
    print("ИТОГО:", all_sum)
    print("Больше всего потрачено на:", top_category)


def main():
    expenses = []
    while True:
        print("\n1 — добавить трату | 2 — отчёт | 0 — выход")
        choice = input("Выбор: ").strip()
        if choice == "1":
            category = input("Категория (еда, транспорт...): ")
            amount = parse_amount(input("Сумма: "))
            if add_expense(expenses, category, amount):
                print("Трата добавлена.")
            else:
                print("Ошибка: нужна категория и положительная сумма.")
        elif choice == "2":
            show_report(expenses)
        elif choice == "0":
            print("До встречи!")
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
