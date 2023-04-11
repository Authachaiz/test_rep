import pytest

from main import calculate_price

def calculate_price(num_dozen):

    num_eggs = num_dozen * 12
    price_per_egg = 4
    if num_dozen < 5:
        price_per_egg = 3
    elif num_dozen >= 5:
        price_per_egg = 35 / 12
    total_price = num_eggs * price_per_egg
    return total_price

