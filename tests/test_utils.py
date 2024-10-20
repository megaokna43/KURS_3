from src.utils import reformated_date, mask_requisites


def test_reformated_date():
    assert  reformated_date ("2019-08-26") == "26.08.2019"

def test_mask_requisites_account():
    assert mask_requisites ("Счет 19708645243227258542") == "Счет **8542"

def test_mask_requisites_recvizits():
    assert mask_requisites ("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"
