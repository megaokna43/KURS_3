from src.utils import reformated_date, mask_requisites, display_last_operations


def test_reformated_date():
    assert reformated_date ("2019-08-26") == "26.08.2019"


def test_mask_requisites_account():
    assert mask_requisites ("Счет 19708645243227258542") == "Счет **8542"


def test_mask_requisites_requisites():
    assert mask_requisites ("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"


def test_executed_display_last_operations(operations):
    for op in display_last_operations(operations):
        assert op['state'] == "EXECUTED"


def test_no_executed_display_last_operations():
    assert display_last_operations () == 'CANCELED'


def test_empty_display_last_operations():
    assert display_last_operations () == None

