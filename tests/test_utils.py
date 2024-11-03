
import pytest
from src.utils import reformated_date, mask_requisites, load_operations, get_last_5_operations


def test_reformated_date():
    assert reformated_date("2019-08-26") == "26.08.2019"


def test_mask_requisites_account():
    assert mask_requisites("Счет 19708645243227258542") == "Счет **8542"


def test_mask_requisites_requisites():
    assert mask_requisites("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"


def test_get_last_5_executed_operations():
    op = load_operations('../operations.json')
    op = op[:5]
    assert len(op) == min(5, len([x for x in op if x['state'] == 'EXECUTED']))


def test_load():
    op = load_operations('../operations.json')
    assert len(op) >= 0


def test_load_wrong():
    op = load_operations('../wrong.json')
    assert len(op) == 0


def test_executed_operations():
    operations = []
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    assert len(executed_operations) == 0


def test_TypeError_get_last_5_operations():
    with pytest.raises(TypeError):
        get_last_5_operations()


def test_AttributeError_get_last_5_operations():
    with pytest.raises(AttributeError):
       get_last_5_operations("    ").non_existent_attribute