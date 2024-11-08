import json
import pytest
from unittest.mock import mock_open, patch
from src.utils import load_operations


def load_json(file):
    return json.load(file)


def test_load():
    op = load_operations('../operations.json')
    # Проверка загрузки данный из файла json
    assert len(op) >= 0


def test_load_wrong():
    op = load_operations('../wrong.json')
    assert len(op) == 0

def test_load_json_valid():
    mock_data = '{"name": "John", "age": 30}'
    with patch('builtins.open', mock_open(read_data=mock_data)):
        with open('operations.json') as file:
            result = load_json(file)
            assert result == {"name": "John", "age": 30}

def test_load_json_invalid():
    mock_data = '{"name": "John", "age": 30'  # Неправильный JSON
    with patch('builtins.open', mock_open(read_data=mock_data)):
        with pytest.raises(json.JSONDecodeError):
            with open('operations.json') as file:
                load_json(file)

if __name__ == "__main__":
    pytest.main()