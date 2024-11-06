import pytest

from src.utils import (reformated_date, mask_requisites, load_operations, get_last_5_operations)


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


def test_load():
    op = load_operations('../operations.json')
    # Проверка загрузки данный из файла json
    assert len(op) >= 0


def test_load_wrong():
    op = load_operations('../wrong.json')
    assert len(op) == 0


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
