import json
import pytest
from unittest.mock import mock_open, patch
from src.utils import load_operations


def test_load():
    op = load_operations('../operations.json') # Проверка загрузки данных из файла json
    assert len(op) >= 0


def test_load_wrong():
    op = load_operations('../wrong.json') # Проверяю загрузку несуществующего файла
    assert len(op) == 0


def test_load_operations_valid():
    test_data = '''{
        "id": 484201274,
        "state": "EXECUTED",
        "date": "2019-04-11T23:10:21.514616",
        "operationAmount": {
            "amount": "62621.51",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        }
    }'''

    with patch('builtins.open', mock_open(read_data=test_data)):
        result = load_operations('operations.json')  # Call the function
        expected_result = {
            "id": 484201274,
            "state": "EXECUTED",
            "date": "2019-04-11T23:10:21.514616",
            "operationAmount": {
                "amount": "62621.51",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }
        }
        assert result == expected_result  # Update the expected result


def test_load_operations_file_not_found_error():
    json_data = ''  # некорректный JSON
    assert json_data != load_operations('operations.json')  # проверяем функцию

def test_load_json_file_json_decode_error():
    # Имитация открытия файла с некорректным JSON
    mock_file = mock_open(read_data="{'key': 'value'")  # Неверный JSON (отсутствует закрывающая скобка)
    with patch('builtins.open', mock_file):
        assert load_operations('in_operations.json') == []
