from src.utils import reformated_date, mask_requisites, display_last_operations, load_operations, get_last_5_operations


def test_reformated_date():
    assert reformated_date("2019-08-26") == "26.08.2019"


def test_mask_requisites_account():
    assert mask_requisites("Счет 19708645243227258542") == "Счет **8542"


def test_mask_requisites_requisites():
    assert mask_requisites("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"


def test_get_last_5_operations():
    op = load_operations('../operations.json')
    op = get_last_5_operations(op)
    assert len(op) == 5


def test_load():
    op = load_operations('../operations.json')
    assert len(op) > 0


def test_load_2():
    op = load_operations('../wrong.json')
    assert len(op) == 0