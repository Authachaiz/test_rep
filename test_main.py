# test_main.py
import pytest
from main import calculate_price

def test_calculate_price_when_buying_1_egg():
    num_dozen = 1
    expected_price = 4
    assert calculate_price(num_dozen) == expected_price

def test_calculate_price_when_buying_1_dozen():
    num_dozen = 12
    expected_price = 36
    assert calculate_price(num_dozen) == expected_price

def test_calculate_price_when_buying_3_dozen():
    num_dozen = 36
    expected_price = 108
    assert calculate_price(num_dozen) == expected_price

def test_calculate_price_when_buying_5_dozen_or_more():
    num_dozen = 60
    expected_price = 180
    assert calculate_price(num_dozen) == expected_price

def test_calculate_price_with_negative_num_dozen():
    num_dozen = -1
    with pytest.raises(ValueError) as e:
        calculate_price(num_dozen)
    assert str(e.value) == "โปรดป้อนจำนวนโหลที่มากกว่า 0"


def test_calculate_price_with_string_num_dozen():
    with pytest.raises(TypeError) as e:
        num_dozen = "abc" 
        calculate_price(num_dozen)
    assert str(e.value) == "'<' not supported between instances of 'str' and 'int'"