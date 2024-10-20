import pytest
import json
from unittest.mock import patch, mock_open
from main import load_operations, display_last_operations


# Тесты для функции load_operations
def test_load_operations_success():
    mock_data = json.dumps([
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2021-01-01T00:00:00",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Тестовая операция",
            "from": "MasterCard 1234567812345678",
            "to": "Счет 1234567890123456"
        }
    ])

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_operations('test.json')
        assert len(result) == 1
        assert result[0]['description'] == "Тестовая операция"


def test_load_operations_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_operations('non_existent_file.json')
        assert result == []


def test_load_operations_json_decode_error():
    with patch("builtins.open", mock_open(read_data="invalid json")):
        result = load_operations('invalid.json')
        assert result == []


# Тесты для функции display_last_operations
def test_display_last_operations(capsys):
    operations = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2021-01-01T00:00:00",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Тестовая операция",
            "from": "MasterCard 1234567812345678",
            "to": "Счет 1234567890123456"
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2021-01-02T00:00:00",
            "operationAmount": {
                "amount": "200.00",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Другая операция",
            "from": "Visa 8765432187654321",
            "to": "Счет 6543210987654321"
        }
    ]

    display_last_operations(operations)

    captured = capsys.readouterr()
    assert "2021-01-02" in captured.out
    assert "Другая операция" in captured.out
    assert "8765 4321 **** 4321" in captured.out
    assert "Счет **4321" in captured.out
    assert "Сумма: 200.00 USD" in captured.out


def test_display_last_operations_no_executed(capsys):
    operations = [
        {
            "id": 1,
            "state": "CANCELED",
            "date": "2021-01-01T00:00:00",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Отмененная операция",
            "from": "MasterCard 1234567812345678",
            "to": "Счет 1234567890123456"
        }
    ]

    display_last_operations(operations)

    captured = capsys.readouterr()
    assert "Не указана" in captured.out  # Проверяем, что выводится "Не указано" для карты и счета


if __name__ == "__main__":
    pytest.main()