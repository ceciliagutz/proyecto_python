from hypothesis import given
from hypothesis.strategies import builds, floats, integers, lists

from intermediate_level.laboratory9 import calculate_order_total


def test_calculate_order_total_simple():
    items = [
        {"price": 1800.0, "quantity": 2},
        {"price": 350.0, "quantity": 1},
    ]
    assert calculate_order_total(items) == 3950.0


def item_strategy():
    return builds(
        lambda price, quantity: {"price": price, "quantity": quantity},
        floats(min_value=0, max_value=4000),
        integers(min_value=1, max_value=10),
    )


@given(lists(item_strategy()))
def test_total_is_non_negative(items):
    total = calculate_order_total(items)
    assert total >= 0
