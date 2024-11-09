import pytest
from src.utils import reformated_date, mask_requisites, get_last_5_operations, load_operations


def test_reformated_date():
    # Проверяем правильность отображения даты
    assert reformated_date("2019-08-26") == "26.08.2019"


def test_mask_requisites_account():
    # Проверяем маскировку данных счета
    assert mask_requisites("Счет 19708645243227258542") == "Счет **8542"


def test_mask_requisites_requisites():
    # Проверяем маскировку реквизитов
    assert mask_requisites("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"


def test_get_last_5_executed_operations():
    op = load_operations('../operations.json')
    # Загрузка операций из файла
    op = op[:5]
    # Делаем срез последних 5 операций
    assert len(op) == min(5, len([x for x in op if x['state'] == 'EXECUTED']))
    # Проверяем что эти операции имеют атрибут 'EXECUTED'


def test_executed_operations():
    # Создание пустого списка операций
    operations = []

    # Фильтрация операций по состоянию 'EXECUTED'
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']

    # Проверка, что список выполненных операций пуст
    assert len(executed_operations) == 0


def test_type_error_get_last_5_operations():
    with pytest.raises(TypeError):
        get_last_5_operations(123)  # Передача целого числа вместо строки


def test_attribute_error_get_last_5_operations():
    with pytest.raises(AttributeError):
        result = get_last_5_operations(" ")  # Вызов функции с пустой строкой
        assert isinstance(result.non_existent_attribute, object)  # Проверка наличия несуществующего атрибута


def test_main_amount_format():
    operations = []
    for x in operations:
        try:
            float(x.operationAmount["amount"])
        except ValueError:
            assert False, f"Сумма '{x.operationAmount['amount']}' не является числом"


def test_main_currency_code():
    operations = []
    for x in operations:
        assert x.operationAmount["currency"]["code"] in ["USD",
                                                         "RUB"], \
            (f"Код валюты '{x.operationAmount['currency']['code']}' "
             f"\n не является ни 'USD', ни 'RUB'")


def test_get_last_5_operations():
    data_set_operations = [{
        "id": 988276204,
        "state": "EXECUTED",
        "date": "2018-02-22T00:40:19.984219",
        "operationAmount": {
            "amount": "71771.90",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 4956649687637418",
        "to": "Счет 90562872508279542248"
    }]

    # Получаем последние 5 операций
    executed_operations = get_last_5_operations(data_set_operations)
    # Сортируем операции по дате
    executed_operations_sorted = sorted(executed_operations, key=lambda x: x.get('date', ''), reverse=True)
    # Проверяем, что возвращаемые операции совпадают с ожидаемыми
    assert executed_operations_sorted[:5] == data_set_operations


@pytest.fixture
def sample_operations():
    return [
        {
            "id": 988276204,
            "state": "EXECUTED",
            "date": "2018-02-22T00:40:19.984219",
            "operationAmount": {
                "amount": "71771.90",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 4956649687637418",
            "to": "Счет 90562872508279542248"
        },
        # Add more sample operations as needed
    ]

def test_display_last_operations(sample_operations):
    last_operations = sample_operations  # Replace with data_set_operations() if needed

    # Проверяем, что мы получили не более 5 последних операций
    assert len(last_operations) <= 5, "Должно быть не более 5 операций"

    for op in last_operations:
        date = op.get('date', 'Не указана')[:10]
        result_date = reformated_date(date)
        description = op.get('description', 'Не указано')

        # Проверяем, что дата и описание корректны
        assert result_date is not None, "Дата не должна быть None"
        assert description, f"Описание не должно быть пустым: {description}"

        amount = op.get('operationAmount', {}).get('amount')
        currency = op.get('operationAmount', {}).get('currency', {}).get('name')

        # Проверяем, что сумма и валюта корректны
        assert amount, f"Сумма не должна быть пустой: {amount}"
        assert currency, f"Валюта не должна быть пустой: {currency}"

        requisites_from = op.get('from', '')
        hidden_from = mask_requisites(requisites_from) if requisites_from else ''

        requisites_to = op.get('to', '')
        hidden_to = mask_requisites(requisites_to)

        # Проверяем, что скрытые реквизиты корректны
        assert hidden_from is not None, "Скрытые реквизиты 'from' не должны быть None"
        assert hidden_to is not None, "Скрытые реквизиты 'to' не должны быть None"
