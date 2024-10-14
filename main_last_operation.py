import json


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


def mask_requisites(requisites:str): # Преобразую данные по счетам с маркировкой
    parts = requisites.split()
    number = parts[-1]
    if requisites.lower().startswith('счет'):
        hidden_number = f"**{number[-4:]}"
    else:
        hidden_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    parts[-1] = hidden_number
    result = ' '.join(parts)
    return result


def reformated_date(date: str): # Преобразую данные даты
    parts_date = date.split('-')
    reversed_date = parts_date[::-1]
    result_date = '.'.join(reversed_date)
    return result_date


def display_last_operations(operations):
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']  # Фильтруем выполненные операции
    executed_operations.sort(key=lambda x: x.get('date', ''), reverse=True)  # Сортируем операции по дате
    last_operations = executed_operations[:5]  # Берем последние 5 операций

    for op in last_operations:  # Выводим информацию о каждой операции
        date = op.get('date', 'Не указана')[:10]
        result_date = reformated_date(date)
        description = op.get('description', 'Не указано')
        print(f"{result_date} {description}")

        amount = op.get('operationAmount').get('amount')
        currency = op.get('operationAmount').get('currency').get('name')
        print(f"{amount} {currency}")

        requisites_from = op.get('from', '')  # Получаем данные откуда
        if requisites_from:
            hidden_from = mask_requisites(requisites_from)
        else:
            hidden_from = ''

        requisites_to = op.get('to', '')  # Получаем данные откуда
        hidden_to = mask_requisites(requisites_to)

        print(f"{hidden_from} -> {hidden_to}")
        print()


def main():
    operations = load_operations('operations.json')
    display_last_operations(operations)


if __name__ == "__main__":
    main()
