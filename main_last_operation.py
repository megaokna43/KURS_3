import json
import re


def load_operations(filename):  # Извлекаем данные из файла
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка при чтении файла {filename}.")
        return []


def display_last_operations(operations):
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']  # Фильтруем выполненные операции
    executed_operations.sort(key=lambda x: x.get('date', ''), reverse=True)  # Сортируем операции по дате
    last_operations = executed_operations[:5]  # Берем последние 5 операций

    for op in last_operations: # Выводим информацию о каждой операции
        print(f"{op.get('date', 'Не указана')[:10]} Описание: {op.get('description', 'Не указано')}")
        amount = op.get('operationAmount', {})
        currency = amount.get('currency', {})
        card_number = op.get('from', '')  # Маскируем данные карты
        match = re.search(r'\d{16}', card_number)  # Ищем 16-значный номер карты

        if match:
            card_number = match.group(0)  # Извлекаем номер карты
            card_number = ' '.join([card_number[i:i + 4] for i in range(0, len(card_number), 4)])  # Форматируем номер
            masked_card_number = f"{card_number[:7]}** **** {card_number[-4:]}"  # Маскируем данные карты

        else:
            masked_card_number = "Не указано"

        account_number = op.get('to', '')
        if isinstance(account_number, str) and len(account_number) >= 6:
            masked_account_number = f"Счет **{account_number[-4:]}"  # Маскируем данные счета
        else:
            masked_account_number = "Не указано"

        print(f"{masked_card_number} -> {masked_account_number}")
        print(f"Сумма: {amount.get('amount', 'Не указана')} {currency.get('name', 'Не указана')}")
        print(' ' * 50)


def main():
    operations = load_operations('operations.json')
    display_last_operations(operations)


if __name__ == "__main__":
    main()
