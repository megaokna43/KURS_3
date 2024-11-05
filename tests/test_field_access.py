import pytest


@pytest.fixture
def example_data():
    return [{
        "id": 608117766,
        "state": "CANCELED",
        "date": "2018-10-08T09:05:05.282282",
        "operationAmount": {
            "amount": "77302.31",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Gold 6527183396477720",
        "to": "Счет 38573816654581789611"
    },
        # выбрал часть данных файла json
    ]


def test_field_access(example_data):
    operation = example_data[0]
    assert operation["id"] == 608117766
    assert operation["state"] == "CANCELED"
    assert operation["date"] == "2018-10-08T09:05:05.282282"
    assert operation["operationAmount"] == {
        "amount": "77302.31",
        "currency": {"name": "USD", "code": "USD"},
    }
    assert operation["description"] == "Перевод с карты на счет"
    assert operation["from"] == "Visa Gold 6527183396477720"
    assert operation["to"] == "Счет 38573816654581789611"

